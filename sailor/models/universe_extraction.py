

from ..utils import open_json_data
from ..exceptions import *

# Libraries
from flashtext import KeywordProcessor
import seaborn as sns





class Universe:
    """A universe can be defined as multiple concepts describing this universe. 
    Each concept can be described as a set of keywordss 
    """
    def __init__(self,data,case_sensitive=False):

        # Store as argumentss
        self.case_sensitive = case_sensitive

        # Open universe data from json file or dict
        if isinstance(data,str) and data.endswith(".json"):
            self.data = open_json_data(data)
        elif isinstance(data,dict):
            self.data = data
        else:
            raise UniverseError("Input universe is not recognized (must be a json path or a dictionary)")

        # Safe check that all concepts have a list of keywords associated
        assert all([isinstance(value,list) for key,value in self.data.items()]),"All values in the dictionary must be lists"

        self.data = {key.upper():value for key,value in self.data.items()}

        # Prepare keyword detector
        self.prepare_keyword_finder(case_sensitive)

        # Prepare colors
        self.prepare_colors()


    def prepare_colors(self):

        # Helper function to convert to hexadecimal colors
        convert_hex = lambda r,g,b : '#%02x%02x%02x' % tuple(map(lambda x : int(x*255),(r,g,b)))
        concepts = list(self.data.keys())

        self.colors = sns.color_palette("husl", len(concepts))
        self.colors = {concepts[i]:convert_hex(*self.colors[i]) for i in range(len(concepts))}


    def prepare_keyword_finder(self,case_sensitive = False):
        self.finder = KeywordProcessor(case_sensitive = case_sensitive)
        self.finder.add_keywords_from_dict(self.data)


    def find_concepts(self,text,unique = False,span_info = False):
        concepts = self.finder.extract_keywords(text,span_info = span_info)
        if unique:
            concepts = list(set(concepts))
        return concepts


    def show_concepts(self,text):
        """Show entities in Jupyter notebook
        Documentation at https://spacy.io/usage/visualizers
        """

        from spacy import displacy

        if isinstance(text,str):

            # Extract all entities
            concepts = self.find_concepts(text,span_info = True)
            concepts = [{"start":concept[1],"end":concept[2],"label":concept[0]} for concept in concepts]

            # Build input dictionary
            data = {
                "text":text,
                "ents":concepts,
                "title":None
            }

            # Build options dictionary
            options = {}
            options["colors"] = self.colors
            options["ents"] = list(self.colors.keys())

            # Render Displacy
            return displacy.render(data,style = "ent",manual = True,jupyter = True,options = options)

        else:
            for document in text:
                self.show_concepts(document)
                print("")


