import unicodedata
import epitran
import epitran.backoff
import indic_transliteration
import indic_transliteration.sanscript

def normalize_text(text):
    return unicodedata.normalize('NFC', text)

def iast_to_devanagari(text):
    transliterate = indic_transliteration.sanscript.transliterate
    iast = indic_transliteration.sanscript.IAST
    deva = indic_transliteration.sanscript.DEVANAGARI
    return transliterate(text, iast, deva)

def devanagari_to_ipa_xsampa(text):
    transliterator = epitran.backoff.Backoff(['hin-Deva', 'eng-Latn'])
    ipa = transliterator.transliterate(text)
    xsampa_list = transliterator.xsampa_list(text)
    xsampa_string = ' '.join(xsampa_list)
    return ipa, xsampa_string

# Example usage
text = """
śakti sahita gaṇapatim śaṃkarādi sēvitaṃ vi
rakta sakala munivarasura rāja vinuta guruguhaṃ
bhaktā ḷi pōṣakam bhavasutaṃ vināyakam
bhukti mukti pradam bhūṣitam gam rakta pādāmbujam bhāvayāmi
"""
print("IAST:", text)

normalized_text = normalize_text(text).lower()
print("Normalized:", normalized_text)

devanagari_text = iast_to_devanagari(normalized_text)
print("Deva:", devanagari_text)

ipa_text = devanagari_to_ipa_xsampa(devanagari_text)[0]
print("IPA:", ipa_text)

xsampa_text = devanagari_to_ipa_xsampa(devanagari_text)[1]
print("XSAMPA:", xsampa_text)
