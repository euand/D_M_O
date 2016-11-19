# -*- coding: utf-8 -*-

from huffman import *
from math import log, ceil

Hamlet = u'O all you host of heaven! O earth! What else? And shall I couple hell? Oh, fie! Hold, hold, my heart, And you, my sinews, grow not instant old, But bear me stiffly up. Remember thee! Ay, thou poor ghost, whiles memory holds a seat In this distracted globe. Remember thee! Yea, from the table of my memory I’ll wipe away all trivial fond records, All saws of books, all forms, all pressures past That youth and observation copied there, And thy commandment all alone shall live Within the book and volume of my brain, Unmixed with baser matter. Yes, by heaven! O most pernicious woman! O villain, villain, smiling, damned villain! My tables! Meet it is I set it down That one may smile, and smile, and be a  villain. At least I’m sure it may be so in Denmark. So, uncle, there you are. Now to my word.'.lower()

Goethe = u'Habe nun, ach! Philosophie, Juristerei und Medizin, Und leider auch Theologie Durchaus studiert, mit heissem Bemühn. Da steh ich nun, ich armer Tor! Und bin so klug als wie zuvor; Heisse Magister, heisse Doktor gar Und ziehe schon an die zehen Jahr Herauf, herab und quer und krumm Meine Schüler an der Nase herum Und sehe, dass wir nichts wissen können! Das will mir schier das Herz verbrennen. Zwar bin ich gescheiter als all die Laffen, Doktoren, Magister, Schreiber und Pfaffen; Mich plagen keine Skrupel noch Zweifel, Fürchte mich weder vor Hölle noch Teufel Dafür ist mir auch alle Freud entrissen, Bilde mir nicht ein, was Rechts zu wissen, Bilde mir nicht ein, ich könnte was lehren, Die Menschen zu bessern und zu bekehren. Auch hab ich weder Gut noch Geld, Noch Ehr und Herrlichkeit der Welt; Es möchte kein Hund so länger leben! Drum hab ich mich der Magie ergeben, Ob mir durch Geistes Kraft und Mund Nicht manch Geheimnis würde kund; Dass ich nicht mehr mit saurem Schweiss Zu sagen brauche, was ich nicht weiss; Dass ich erkenne, was die Welt Im Innersten zusammenhält, Schau alle Wirkenskraft und Samen, Und tu nicht mehr in Worten kramen.'.lower()


def test_alph_count():
    text = 'foobar'
    count = alph_count(text)
    assert(type(count) is list)
    assert(isinstance(count[0], Tree))

def test_huffman_code():
    text = 'foo'
    code = huffman_code('foo')
    assert(type(code) is list)
    assert(code == [('0', 'f'), ('1', 'o')])

def test_huffman_worst_case():
    text = 'abcdefghijklmnopqrstuvwxyz'
    code = huffman_code(text)
    coded = huffman_encode(code, text)
    N = len(text)
    assert(len(coded) <= (N * ceil(log(N, 2))))

def test_huffman_decode():
    code = huffman_code(Hamlet)
    coded = huffman_encode(code, Hamlet)
    decoded = huffman_decode(code, coded)
    assert(decoded == Hamlet)
