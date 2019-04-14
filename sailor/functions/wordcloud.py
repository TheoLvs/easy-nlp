
from wordcloud import WordCloud

def plot_word_cloud(text,title = "",width = 600,height = 300,max_words = 50,figsize = (18,10),max_font_size = 50,mask_file = None,**kwargs):

    with plt.style.context(('ggplot')):
        fig = plt.figure(figsize=figsize)
        if mask_file is not None:
            mask = np.array(Image.open(mask_file))
        else:
            mask = None
        wordcloud = WordCloud(background_color='white', width=width, height=height,
                        max_font_size=max_font_size, max_words=max_words,
                        mask = mask,**kwargs).generate(text)
        wordcloud.recolor(random_state=0)
        plt.imshow(wordcloud,interpolation = "bilinear")
        plt.title(title, fontsize=20)
        plt.axis("off")
        plt.show()
        
    return fig
