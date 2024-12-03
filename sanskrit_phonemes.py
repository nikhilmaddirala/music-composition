import unicodedata
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import epitran

def normalize_text(text):
    return unicodedata.normalize('NFC', text)

def iast_to_devanagari(text):
    return transliterate(text, sanscript.IAST, sanscript.DEVANAGARI)

def devanagari_to_ipa(text):
    epi = epitran.Epitran('hin-Deva')  # 'hin-Deva' is the code for Hindi in Devanagari script
    return epi.transliterate(text)

def iast_to_ipa_transliterate(text):
    devanagari_text = iast_to_devanagari(text)
    ipa_text = devanagari_to_ipa(devanagari_text)
    return ipa_text

# Example usage
text = "hariḥ om | omityetadakṣaramidaṃ sarvaṃ tasyopavyākhyānaṃ bhūtaṃ bhavadbhaviṣyaditi sarvamoṅkāra eva | yaccānyattrikālātītaṃ tadapyoṅkāra eva"
normalized_text = normalize_text(text).lower()
ipa_transliteration = iast_to_ipa_transliterate(normalized_text)
print("IAST:", text)
print("Deva:", iast_to_devanagari(text))
print("IPA transliteration:", ipa_transliteration)