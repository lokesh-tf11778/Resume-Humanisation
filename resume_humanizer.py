import re
import random
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
import textstat

class ResumeHumanizer:
    def __init__(self):
        # Download required NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        
        # AI detection patterns
        self.ai_patterns = [
            r'\b(utilized|leveraged|implemented|orchestrated|spearheaded|pioneered|architected)\b',
            r'\b(streamlined|optimized|enhanced|facilitated|coordinated|managed|delivered)\b',
            r'\b(resulted in|led to|achieved|attained|maintained|improved|increased)\b',
            r'\b(collaborated with|worked with|partnered with|coordinated with)\b',
            r'\b(ensured|guaranteed|validated|verified|confirmed|established)\b',
            r'\b(developed|created|built|designed|constructed|formulated)\b',
            r'\b(analyzed|evaluated|assessed|reviewed|examined|investigated)\b',
            r'\b(provided|delivered|supplied|offered|presented|submitted)\b',
            r'\b(monitored|tracked|oversaw|supervised|guided|mentored)\b',
            r'\b(resolved|addressed|solved|fixed|corrected|remedied)\b'
        ]
        
        # Human alternatives
        self.human_alternatives = {
            'utilized': ['used', 'employed', 'applied', 'worked with'],
            'leveraged': ['used', 'took advantage of', 'made use of'],
            'implemented': ['put in place', 'set up', 'started', 'began'],
            'orchestrated': ['organized', 'arranged', 'planned', 'coordinated'],
            'spearheaded': ['led', 'headed', 'started', 'initiated'],
            'pioneered': ['started', 'began', 'introduced', 'created'],
            'architected': ['designed', 'planned', 'created', 'built'],
            'streamlined': ['simplified', 'made easier', 'improved', 'organized'],
            'optimized': ['improved', 'made better', 'enhanced', 'refined'],
            'enhanced': ['improved', 'made better', 'upgraded', 'strengthened'],
            'facilitated': ['helped', 'made possible', 'enabled', 'assisted'],
            'coordinated': ['organized', 'arranged', 'managed', 'oversaw'],
            'managed': ['oversaw', 'supervised', 'led', 'handled'],
            'delivered': ['provided', 'gave', 'supplied', 'offered'],
            'resulted in': ['led to', 'caused', 'brought about', 'created'],
            'led to': ['caused', 'resulted in', 'brought about', 'created'],
            'achieved': ['reached', 'attained', 'accomplished', 'gained'],
            'attained': ['reached', 'achieved', 'gained', 'obtained'],
            'maintained': ['kept', 'preserved', 'sustained', 'continued'],
            'improved': ['made better', 'enhanced', 'upgraded', 'strengthened'],
            'increased': ['raised', 'boosted', 'enhanced', 'grew'],
            'collaborated with': ['worked with', 'partnered with', 'teamed up with'],
            'worked with': ['partnered with', 'collaborated with', 'teamed up with'],
            'partnered with': ['worked with', 'collaborated with', 'teamed up with'],
            'coordinated with': ['worked with', 'organized with', 'arranged with'],
            'ensured': ['made sure', 'guaranteed', 'confirmed', 'verified'],
            'guaranteed': ['ensured', 'made sure', 'promised', 'assured'],
            'validated': ['confirmed', 'verified', 'checked', 'tested'],
            'verified': ['confirmed', 'checked', 'tested', 'validated'],
            'confirmed': ['verified', 'checked', 'tested', 'validated'],
            'established': ['set up', 'created', 'founded', 'started'],
            'developed': ['created', 'built', 'made', 'designed'],
            'created': ['made', 'built', 'developed', 'designed'],
            'built': ['created', 'made', 'developed', 'constructed'],
            'designed': ['created', 'planned', 'developed', 'made'],
            'constructed': ['built', 'created', 'made', 'assembled'],
            'formulated': ['created', 'developed', 'designed', 'made'],
            'analyzed': ['examined', 'studied', 'looked at', 'reviewed'],
            'evaluated': ['assessed', 'reviewed', 'examined', 'studied'],
            'assessed': ['evaluated', 'reviewed', 'examined', 'studied'],
            'reviewed': ['examined', 'looked at', 'studied', 'assessed'],
            'examined': ['looked at', 'studied', 'reviewed', 'analyzed'],
            'investigated': ['looked into', 'studied', 'examined', 'researched'],
            'provided': ['gave', 'supplied', 'offered', 'delivered'],
            'supplied': ['provided', 'gave', 'offered', 'delivered'],
            'offered': ['provided', 'gave', 'supplied', 'presented'],
            'presented': ['gave', 'offered', 'showed', 'displayed'],
            'submitted': ['gave', 'handed in', 'turned in', 'provided'],
            'monitored': ['watched', 'tracked', 'oversaw', 'supervised'],
            'tracked': ['monitored', 'watched', 'followed', 'oversaw'],
            'oversaw': ['supervised', 'managed', 'watched over', 'guided'],
            'supervised': ['oversaw', 'managed', 'guided', 'led'],
            'guided': ['led', 'directed', 'helped', 'assisted'],
            'mentored': ['guided', 'helped', 'taught', 'coached'],
            'resolved': ['solved', 'fixed', 'addressed', 'handled'],
            'addressed': ['dealt with', 'handled', 'solved', 'fixed'],
            'solved': ['fixed', 'resolved', 'handled', 'addressed'],
            'fixed': ['solved', 'resolved', 'corrected', 'repaired'],
            'corrected': ['fixed', 'repaired', 'amended', 'adjusted'],
            'remedied': ['fixed', 'corrected', 'solved', 'resolved']
        }
    
    def humanize_resume(self, text):
        """Transform AI-generated resume text to appear human-written."""
        # Step 1: Replace AI patterns with human alternatives
        text = self._replace_ai_patterns(text)
        
        # Step 2: Add natural variations and imperfections
        text = self._add_human_variations(text)
        
        # Step 3: Improve sentence structure and flow
        text = self._improve_sentence_structure(text)
        
        # Step 4: Add personal touches and natural language
        text = self._add_personal_touches(text)
        
        return text
    
    def _replace_ai_patterns(self, text):
        """Replace AI-generated patterns with more human alternatives."""
        for pattern in self.ai_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                original_word = match.group().lower()
                if original_word in self.human_alternatives:
                    alternatives = self.human_alternatives[original_word]
                    replacement = random.choice(alternatives)
                    text = text[:match.start()] + replacement + text[match.end():]
        
        return text
    
    def _add_human_variations(self, text):
        """Add natural variations that make text appear more human."""
        # Add some sentence variations
        sentences = sent_tokenize(text)
        humanized_sentences = []
        
        for sentence in sentences:
            # Occasionally add natural connectors
            if random.random() < 0.3:
                connectors = ['Also, ', 'Additionally, ', 'Furthermore, ', 'Moreover, ']
                sentence = random.choice(connectors) + sentence
            
            # Occasionally use contractions
            if random.random() < 0.4:
                sentence = sentence.replace(' I am ', ' I\'m ')
                sentence = sentence.replace(' I have ', ' I\'ve ')
                sentence = sentence.replace(' I will ', ' I\'ll ')
                sentence = sentence.replace(' I would ', ' I\'d ')
            
            humanized_sentences.append(sentence)
        
        return ' '.join(humanized_sentences)
    
    def _improve_sentence_structure(self, text):
        """Improve sentence structure to sound more natural."""
        # Break up very long sentences
        sentences = sent_tokenize(text)
        improved_sentences = []
        
        for sentence in sentences:
            if len(sentence.split()) > 25:  # Very long sentence
                # Split on common conjunctions
                parts = re.split(r'\s+(and|or|but|however|therefore)\s+', sentence)
                if len(parts) > 1:
                    improved_sentences.extend(parts)
                else:
                    improved_sentences.append(sentence)
            else:
                improved_sentences.append(sentence)
        
        return ' '.join(improved_sentences)
    
    def _add_personal_touches(self, text):
        """Add personal touches that make the resume feel more human."""
        # Add some personal pronouns occasionally
        text = re.sub(r'\b(Managed|Led|Oversaw)\b', lambda m: random.choice(['I managed', 'I led', 'I oversaw']) if random.random() < 0.2 else m.group(), text)
        
        # Add some natural qualifiers
        qualifiers = ['successfully', 'effectively', 'efficiently', 'consistently']
        for qualifier in qualifiers:
            if random.random() < 0.1:  # 10% chance to add qualifier
                text = text.replace('managed', f'{qualifier} managed', 1)
                break
        
        return text
    
    def get_readability_score(self, text):
        """Calculate readability score to ensure human-like complexity."""
        return {
            'flesch_reading_ease': textstat.flesch_reading_ease(text),
            'flesch_kincaid_grade': textstat.flesch_kincaid_grade(text),
            'gunning_fog': textstat.gunning_fog(text),
            'smog_index': textstat.smog_index(text),
            'automated_readability_index': textstat.automated_readability_index(text),
            'coleman_liau_index': textstat.coleman_liau_index(text),
            'linsear_write_formula': textstat.linsear_write_formula(text),
            'dale_chall_readability_score': textstat.dale_chall_readability_score(text),
            'difficult_words': textstat.difficult_words(text),
            'syllable_count': textstat.syllable_count(text),
            'lexicon_count': textstat.lexicon_count(text),
            'sentence_count': textstat.sentence_count(text)
        }