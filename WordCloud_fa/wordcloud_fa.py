import matplotlib.pyplot as plt
from wordcloud import WordCloud
import arabic_reshaper
from bidi.algorithm import get_display

from fonts.fonts import Fonts
class FarsiWordCloud(Fonts):
    def __init__(self, text, font_name=None, width=800, height=400, background_color='white', max_font_size=250, min_font_size=10):
        super().__init__()
        self.text = text
        self.font_path = self.SetFont(font_name)
        self.width = width
        self.height = height
        self.background_color = background_color
        self.max_font_size = max_font_size
        self.min_font_size = min_font_size
        self.wordcloud = None
        self.reshaped_text = None
        self.bidi_text = None
    
    def reshape_text(self):
        """Reshape and reorder the Farsi (Persian) text for correct display."""
        self.reshaped_text = arabic_reshaper.reshape(self.text)
        self.bidi_text = get_display(self.reshaped_text)
    
    def generate_wordcloud(self):
        """Generate the word cloud based on reshaped text."""
        if not self.bidi_text:
            self.reshape_text()
        self.wordcloud = WordCloud(
            font_path=self.font_path,
            width=self.width,
            height=self.height,
            background_color=self.background_color,
            max_font_size=self.max_font_size,
            min_font_size=self.min_font_size
        ).generate(self.bidi_text)
    
    def show_wordcloud(self):
        """Display the generated word cloud."""
        if self.wordcloud is None:
            self.generate_wordcloud()
        plt.figure(figsize=(self.width / 80, self.height / 80))
        plt.imshow(self.wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
    
    def save_wordcloud(self, filename='wordcloud.png'):
        """Save the generated word cloud to a file."""
        if self.wordcloud is None:
            self.generate_wordcloud()
        self.wordcloud.to_file(filename)
        print(f"Word cloud saved as {filename}")


