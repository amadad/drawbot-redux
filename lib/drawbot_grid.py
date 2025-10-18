"""
DrawBot Grid System - Adapted from mathieureguer/drawbotgrid
Provides grid-based layout helpers for compositional design.

Original: https://github.com/mathieureguer/drawbotgrid
License: All rights reserved (Mathieu Reguer)
Adapted for drawbot-skia compatibility
"""

import drawBot as db
import math

# ==================== CORE GRID CLASSES ====================

class AbstractArea:
    """Base class for all grid areas - manages position and size"""

    def __init__(self, possize):
        self._x, self._y, self._width, self._height = possize

    @classmethod
    def from_margins(cls, margins, *args, **kwargs):
        """Create grid from margin values (left, bottom, right, top) as negative numbers"""
        left_margin, bottom_margin, right_margin, top_margin = margins
        # Get page dimensions from current DrawBot context
        try:
            page_width = db.width()
            page_height = db.height()
        except:
            # Fallback to letter size if no active canvas
            page_width = 612
            page_height = 792
        possize = (-left_margin, -bottom_margin,
                   page_width + left_margin + right_margin,
                   page_height + bottom_margin + top_margin)
        return cls(possize, *args, **kwargs)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def top(self):
        """Absolute Y value of the top of the grid"""
        return self._y + self._height

    @property
    def bottom(self):
        """Absolute Y value of the bottom of the grid"""
        return self.y

    @property
    def left(self):
        """Absolute X value of the left of the grid"""
        return self.x

    @property
    def right(self):
        """Absolute X value of the right of the grid"""
        return self.x + self.width

    @property
    def center(self):
        return self.horizontal_center, self.vertical_center

    @property
    def horizontal_center(self):
        return self.x + self.width / 2

    @property
    def vertical_center(self):
        return self.y + self.height / 2

    draw_color = (1, 0, 1, 1)  # Magenta for grid visualization

    def draw(self, show_index=False):
        """Draw the grid for debugging"""
        with db.savedState():
            db.stroke(*self.draw_color)
            db.fill(None)
            db.strokeWidth(0.5)
            self.draw_frame()

        if show_index:
            with db.savedState():
                db.stroke(None)
                db.fill(*self.draw_color)
                db.fontSize(5)
                self.draw_indexes()

    def draw_frame(self):
        raise NotImplementedError

    def draw_indexes(self):
        raise NotImplementedError


class AbstractGutterGrid(AbstractArea):
    """Base class for grids with gutters (columns/rows)"""

    def __init__(self, possize, subdivisions=8, gutter=10):
        super().__init__(possize)
        self.subdivisions = subdivisions
        self.gutter = gutter

    @property
    def _start_point(self):
        raise NotImplementedError

    @property
    def _end_point(self):
        raise NotImplementedError

    @property
    def _reference_dimension(self):
        return self._end_point - self._start_point

    @property
    def subdivision_dimension(self):
        """The absolute dimension of a single subdivision"""
        return (self._reference_dimension - ((self.subdivisions - 1) * self.gutter)) / self.subdivisions

    def span(self, span):
        """
        The absolute dimension of a span of consecutive subdivisions,
        including their in-between gutters
        """
        assert isinstance(span, (float, int))
        if span >= 0:
            return self.subdivision_dimension * span + self.gutter * (math.ceil(span) - 1)
        else:
            return self.subdivision_dimension * span + self.gutter * (math.ceil(span) + 1)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self[i] for i in range(*key.indices(len(self)))]
        elif isinstance(key, int):
            index = key
            if index >= 0:
                return self._start_point + index * (self.gutter + self.subdivision_dimension)
            else:
                return self._end_point + (index + 1) * (self.gutter + self.subdivision_dimension)

    def __len__(self):
        return self.subdivisions

    def __iter__(self):
        return iter([self.__getitem__(i) for i in range(self.subdivisions)])

    def __mul__(self, factor):
        """Multiply to get span width/height: grid * 3 = width of 3 subdivisions"""
        return self.span(factor)


class ColumnGrid(AbstractGutterGrid):
    """
    Grid for vertical columns.

    Usage:
        columns = ColumnGrid((x, y, w, h), subdivisions=8, gutter=10)
        x_pos = columns[3]        # X coordinate of column 3
        width = columns * 2       # Width of 2 columns + gutter
    """

    @property
    def columns(self):
        return self.subdivisions

    @property
    def column_width(self):
        return self.subdivision_dimension

    @property
    def _start_point(self):
        return self.left

    @property
    def _end_point(self):
        return self.right

    def draw_frame(self):
        for col in self:
            db.rect(col, self.bottom, self.column_width, self.height)

    def draw_indexes(self):
        for i, col in enumerate(self):
            db.text(str(i), (col + 2, self.bottom + 2))


class RowGrid(AbstractGutterGrid):
    """
    Grid for horizontal rows.

    Usage:
        rows = RowGrid((x, y, w, h), subdivisions=8, gutter=10)
        y_pos = rows[2]           # Y coordinate of row 2
        height = rows * 3         # Height of 3 rows + gutters
    """

    @property
    def rows(self):
        return self.subdivisions

    @property
    def row_height(self):
        return self.subdivision_dimension

    @property
    def _start_point(self):
        return self.bottom

    @property
    def _end_point(self):
        return self.top

    def draw_frame(self):
        for row in self:
            db.rect(self.left, row, self.width, self.row_height)

    def draw_indexes(self):
        for i, row in enumerate(self):
            db.text(str(i), (self.left + 2, row + 2))


class Grid(AbstractGutterGrid):
    """
    Combined column and row grid for 2D layout.

    Usage:
        grid = Grid.from_margins((-50, -50, -50, -50),
                                 column_subdivisions=12,
                                 row_subdivisions=8)

        # Get coordinates:
        x, y = grid[(3, 5)]       # Column 3, Row 5

        # Get dimensions:
        w, h = grid*(4, 2)        # 4 columns wide, 2 rows tall

        # Unpack for rect:
        db.rect(*grid[(0, 0)], *grid*(6, 4))
    """

    def __init__(self, possize, column_subdivisions=8, row_subdivisions=8,
                 column_gutter=10, row_gutter=10):
        self._x, self._y, self._width, self._height = possize
        self.columns = ColumnGrid(possize, column_subdivisions, column_gutter)
        self.rows = RowGrid(possize, row_subdivisions, row_gutter)

    @property
    def column_width(self):
        return self.columns.column_width

    @property
    def row_height(self):
        return self.rows.row_height

    @property
    def subdivision_dimension(self):
        return self.column_width, self.row_height

    def column_span(self, span):
        return self.columns.span(span)

    def row_span(self, span):
        return self.rows.span(span)

    def span(self, column_span_row_span):
        """Return (width, height) for a span of (columns, rows)"""
        assert len(column_span_row_span) == 2
        column_span, row_span = column_span_row_span
        return self.column_span(column_span), self.row_span(row_span)

    def __getitem__(self, index):
        """Get (x, y) coordinate for (column_index, row_index)"""
        assert len(index) == 2
        return self.columns[index[0]], self.rows[index[1]]

    def __len__(self):
        return len(self.columns) * len(self.rows)

    def __iter__(self):
        return iter([(c, r) for c in self.columns for r in self.rows])

    def __mul__(self, factor):
        """Multiply by (col_span, row_span) to get (width, height)"""
        return self.span(factor)

    def draw_frame(self):
        for col, row in self:
            db.rect(col, row, self.column_width, self.row_height)

    def draw_indexes(self):
        self.columns.draw_indexes()
        self.rows.draw_indexes()

    def draw(self, show_index=False):
        """Override to draw both column and row grids"""
        self.columns.draw(show_index=show_index)
        self.rows.draw(show_index=show_index)


class BaselineGrid(AbstractArea):
    """
    Grid for text baseline alignment.

    Unlike RowGrid, BaselineGrid:
    - Has no gutter
    - Index [0] is at TOP (for top-down text flow)
    - Has fixed subdivision height (line_height)

    Usage:
        baselines = BaselineGrid.from_margins((0, 0, 0, 0), line_height=16)
        y_pos = baselines[0]      # First line at top
        spacing = baselines * 3   # Height of 3 lines
    """

    def __init__(self, possize, line_height):
        self.input_possize = possize
        super().__init__(possize)
        self.line_height = line_height

    @property
    def _start_point(self):
        return self.top

    @property
    def _end_point(self):
        return self.y

    @property
    def bottom(self):
        """Bottom matches the last visible line"""
        return self[-1]

    @property
    def height(self):
        """Height is actual distance from last to first line"""
        return self.top - self.bottom

    @property
    def _reference_dimension(self):
        return self._end_point - self._start_point

    @property
    def subdivisions(self):
        return abs(int(self._reference_dimension // self.subdivision_dimension)) + 1

    @property
    def subdivision_dimension(self):
        return -self.line_height

    def span(self, span):
        return span * self.subdivision_dimension

    def baseline_index_from_coordinate(self, y_coordinate):
        """Get the baseline index closest to a Y coordinate"""
        for i, line in sorted(enumerate(self)):
            if y_coordinate >= line:
                return i

    def closest_line_below_coordinate(self, y_coordinate):
        """Get the baseline Y value below a coordinate"""
        for i, line in sorted(enumerate(self)):
            if y_coordinate >= line:
                return line

    def closest_line_above_coordinate(self, y_coordinate):
        """Get the baseline Y value above a coordinate"""
        for i, line in sorted(enumerate(self)):
            if y_coordinate > line:
                return line + self.line_height

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self[i] for i in range(*key.indices(len(self)))]
        elif isinstance(key, int):
            index = key
            if index >= 0:
                return self._start_point + index * self.subdivision_dimension
            else:
                return self._start_point + len(self) * self.subdivision_dimension + index * self.subdivision_dimension

    def __len__(self):
        return self.subdivisions

    def __iter__(self):
        return iter([self.__getitem__(i) for i in range(self.subdivisions)])

    def __mul__(self, factor):
        return self.span(factor)

    draw_color = (0, 1, 1, 1)  # Cyan for baseline grids

    def draw_frame(self):
        for baseline in self:
            db.line((self.left, baseline), (self.right, baseline))

    def draw_indexes(self):
        for i, line in enumerate(self):
            db.text(str(i), (self.left + 2, line + 2))


# ==================== CONVENIENCE FUNCTIONS ====================

def create_page_grid(page_width, page_height, margin,
                     column_subdivisions=12, row_subdivisions=8,
                     column_gutter=10, row_gutter=10):
    """
    Create a grid for a full page with equal margins.

    Args:
        page_width, page_height: Page dimensions
        margin: Margin on all sides
        column_subdivisions: Number of columns
        row_subdivisions: Number of rows
        column_gutter, row_gutter: Gutter sizes

    Returns:
        Grid object
    """
    return Grid.from_margins(
        (-margin, -margin, -margin, -margin),
        column_subdivisions=column_subdivisions,
        row_subdivisions=row_subdivisions,
        column_gutter=column_gutter,
        row_gutter=row_gutter
    )


# Note: Text snapping functions (baselineGridTextBox, etc.) not included
# as they require more complex textBox handling not fully compatible with drawbot-skia.
# For drawbot-skia, use the grids for positioning but handle text manually.
