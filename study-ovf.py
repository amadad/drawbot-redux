from drawBot import newPage, textBox, textSize, saveImage, size, stroke, strokeWidth, line, fill, font, text, fontSize

# Set up the letter paper size
size(612, 792)  # 8.5 x 11 inches in points

# Define your long text here
long_text = """Play virtues spirit zarathustra christian. Against fearful faith deceptions self. Salvation justice ubermensch passion faith ultimate love morality gains joy revaluation ideal. Society will grandeur madness good superiority convictions morality inexpedient prejudice decieve right will.

Value ultimate philosophy society snare battle joy moral decrepit. Deceptions moral noble virtues chaos revaluation derive play. Insofar intentions derive sea war horror prejudice.

Of zarathustra morality gains good insofar inexpedient chaos. Suicide superiority horror noble ocean enlightenment love chaos virtues. Christianity against marvelous insofar endless ideal insofar faith disgust christian pinnacle of. Derive eternal-return derive war dead pinnacle pinnacle faith derive ascetic inexpedient ascetic ascetic.

Morality virtues revaluation derive selfish noble of zarathustra. Prejudice god free zarathustra free passion revaluation self justice ultimate burying. Horror prejudice enlightenment revaluation chaos christianity victorious love transvaluation. Reason love against chaos free noble evil ascetic endless revaluation hope. Moral justice aversion truth holiest christian ocean ideal truth decieve noble. Derive ubermensch convictions self horror overcome horror aversion gains ubermensch. Merciful ascetic endless battle war revaluation war battle overcome justice insofar salvation against.

Disgust mountains virtues ocean battle value hope moral. Fearful intentions aversion noble madness reason truth. Passion dead oneself decieve play snare snare. Selfish pinnacle will ideal derive overcome derive superiority horror sea play grandeur morality justice. Of endless law suicide self hope truth marvelous ubermensch snare merciful free. Justice love enlightenment god grandeur faithful gains play contradict.

Intentions christianity philosophy suicide superiority insofar faithful. Sexuality contradict pinnacle derive pinnacle god love strong moral right. Pious self passion god truth faith holiest. Reason law holiest snare deceptions hope dead inexpedient value faithful. Against morality of good virtues grandeur. Derive ultimate moral merciful burying overcome virtues.

Depths transvaluation disgust selfish suicide burying truth convictions of pinnacle ideal society pious ubermensch. War christianity war madness endless love mountains pious horror. Faith play enlightenment enlightenment abstract victorious pious. Holiest derive christian intentions society society spirit pinnacle sea free dead ascetic zarathustra god. Joy gains hatred aversion reason noble joy disgust.

Overcome hatred hope gains ultimate oneself christian abstract ubermensch. Philosophy play hope enlightenment spirit play deceptions virtues oneself spirit hatred ultimate. Self holiest gains noble grandeur burying intentions ocean salvation christianity depths hatred suicide fearful. Oneself aversion madness christian law derive mountains. Zarathustra justice ultimate society right eternal-return self grandeur pinnacle ascetic passion of ocean grandeur. Hatred mountains battle marvelous superiority deceptions aversion value passion play. Marvelous derive insofar deceptions oneself joy faithful god enlightenment philosophy love.

Insofar self self morality deceptions free ubermensch horror evil self virtues moral battle ascetic. Right depths value enlightenment insofar god ultimate gains contradict depths good ubermensch endless oneself. Of ubermensch victorious grandeur intentions virtues fearful derive faithful will contradict merciful. Gains god ubermensch convictions revaluation free pinnacle truth holiest transvaluation suicide ocean mountains snare. Enlightenment intentions spirit contradict holiest zarathustra right decieve.

Hope ascetic god superiority mountains virtues love ubermensch sexuality value self free ubermensch. Dead aversion ideal battle zarathustra salvation ubermensch prejudice justice burying. Transvaluation ultimate victorious free superiority oneself value hatred endless endless convictions virtues justice madness. Dead transvaluation zarathustra evil law philosophy snare merciful salvation ideal will. Value good madness faith disgust suicide. Contradict battle passion endless deceptions right. Horror reason pinnacle burying abstract revaluation.

Morality zarathustra self war ultimate reason depths pious transvaluation aversion. Prejudice derive overcome right abstract contradict sexuality spirit hatred society. Sea suicide suicide aversion fearful dead decrepit faithful ocean. Good evil intentions aversion superiority will revaluation derive. Joy decrepit snare strong decrepit reason. Play of endless reason spirit play snare morality enlightenment marvelous christian suicide right sea.

Christianity overcome god revaluation self self transvaluation contradict."""

# Initial page setup
page_width = 612  # 8.5 inches in points
page_height = 792  # 11 inches in points
margin = 72  # 1 inch margin
text_box_width = page_width - 2 * margin
text_box_height = page_height - 2 * margin - 50  # Leave space for the line and page number

# Set font to TASA Orbiter Text
font_name = "TASA Orbiter Text"  # Replace with the exact name as installed or path to the font file
font_size = 14  # Example font size, adjust as needed
font(font_name)
fontSize(font_size)

# Function to draw the line rule and page number
def add_footer(page_num):
    # Reset stroke for the line
    stroke(0)  # Set line color to black
    strokeWidth(1)  # Set line width
    line((margin, margin - 25), (page_width - margin, margin - 25))  # Draw line
    
    # Reset stroke for the text to ensure it doesn't look bolded/stroked
    stroke(None)  # Disable stroke for text
    fill(0)  # Set text color to black
    font(font_name)  # Ensure font is set for footer as well
    fontSize(font_size)  # Ensure font size is set for footer as well
    text(f"Page {page_num}", (page_width / 2, margin - 45), align="center")  # Draw page number


# Function to draw text and handle overflow
def draw_text_in_box(text, box):
    page_num = 1
    overflow = textBox(text, box)
    add_footer(page_num)
    while overflow:
        page_num += 1
        newPage(page_width, page_height)
        font(font_name)  # Re-apply font settings after newPage
        fontSize(font_size)  # Re-apply font size settings after newPage
        overflow = textBox(overflow, box)
        add_footer(page_num)

# Initial call to draw text
box = (margin, margin + 50, text_box_width, text_box_height)  # Adjusted box to leave space for footer
draw_text_in_box(long_text, box)

saveImage("~/Desktop/Overflow.pdf")
print("A layout study document created with all text in 'TASA Orbiter Text', including line rule and page number.")