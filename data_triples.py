# ─────────────────────────────────────────────────────────────────────────────
# DATA - Triples
# ─────────────────────────────────────────────────────────────────────────────

TRIPLES = [
    # Lines of influence between thinkers
    ("socrates",     "influenced",  "plato"),
    ("plato",        "influenced",  "aristotle"),
    ("aristotle",    "influenced",  "kant"),
    ("kant",         "influenced",  "hegel"),
    ("kant",         "influenced",  "wittgenstein"),
    ("hegel",        "influenced",  "marx"),
    ("hegel",        "influenced",  "nietzsche"),
    ("hegel",        "influenced",  "heidegger"),
    ("nietzsche",    "influenced",  "heidegger"),
    ("heidegger",    "influenced",  "sartre"),
    ("sartre",       "influenced",  "camus"),
    ("marx",         "influenced",  "engels"),
    ("wittgenstein", "influenced",  "russell"),
    ("nietzsche",    "influenced",  "foucault"),
    ("heidegger",    "influenced",  "derrida"),

    # Concepts each thinker developed
    ("plato",        "developed",   "the_forms"),
    ("plato",        "developed",   "logos"),
    ("kant",         "developed",   "categorical_imperative"),
    ("hegel",        "developed",   "dialectic"),
    ("hegel",        "developed",   "idealism"),
    ("marx",         "developed",   "materialism"),
    ("nietzsche",    "developed",   "will_to_power"),
    ("wittgenstein", "developed",   "language_games"),
    ("heidegger",    "developed",   "being"),
    ("sartre",       "developed",   "existentialism"),
    ("camus",        "developed",   "absurdism"),
    ("russell",      "developed",   "logical_atomism"),
    ("foucault",     "developed",   "power_knowledge"),
    ("derrida",      "developed",   "deconstruction"),
    ("engels",       "developed",   "dialectical_materialism"),

    # Concepts each thinker critiqued
    ("aristotle",    "critiqued",   "the_forms"),
    ("marx",         "critiqued",   "idealism"),
    ("nietzsche",    "critiqued",   "categorical_imperative"),
    ("wittgenstein", "critiqued",   "logos"),
    ("camus",        "critiqued",   "existentialism"),
    ("russell",      "critiqued",   "language_games"),
    ("foucault",     "critiqued",   "materialism"),
    ("derrida",      "critiqued",   "logos"),

    # Teaching relationships
    ("socrates",     "taught",      "plato"),
    ("plato",        "taught",      "aristotle"),
    ("hegel",        "taught",      "marx"),
    ("husserl",      "taught",      "heidegger"),
    ("heidegger",    "taught",      "arendt"),
    ("sartre",       "taught",      "beauvoir"),
    ("russell",      "taught",      "wittgenstein"),

    # Opposition between thinkers
    ("marx",         "opposed",     "hegel"),
    ("nietzsche",    "opposed",     "socrates"),
    ("sartre",       "opposed",     "camus"),
    ("russell",      "opposed",     "heidegger"),
    ("popper",       "opposed",     "marx"),
    ("camus",        "opposed",     "marx"),
    ("derrida",      "opposed",     "russell"),

    # School of thought membership
    ("plato",        "belongs_to",  "idealism"),
    ("aristotle",    "belongs_to",  "empiricism"),
    ("marx",         "belongs_to",  "materialism"),
    ("sartre",       "belongs_to",  "existentialism"),
    ("camus",        "belongs_to",  "absurdism"),
    ("wittgenstein", "belongs_to",  "analytic_philosophy"),
    ("russell",      "belongs_to",  "analytic_philosophy"),
    ("heidegger",    "belongs_to",  "continental_philosophy"),
    ("derrida",      "belongs_to",  "continental_philosophy"),
    ("foucault",     "belongs_to",  "post_structuralism"),

    # Key written works
    ("plato",        "wrote",       "the_republic"),
    ("aristotle",    "wrote",       "nicomachean_ethics"),
    ("kant",         "wrote",       "critique_of_pure_reason"),
    ("hegel",        "wrote",       "phenomenology_of_spirit"),
    ("marx",         "wrote",       "das_kapital"),
    ("nietzsche",    "wrote",       "thus_spoke_zarathustra"),
    ("wittgenstein", "wrote",       "tractatus_logico_philosophicus"),
    ("heidegger",    "wrote",       "being_and_time"),
    ("sartre",       "wrote",       "being_and_nothingness"),
    ("camus",        "wrote",       "the_myth_of_sisyphus"),
    ("foucault",     "wrote",       "discipline_and_punish"),
    ("derrida",      "wrote",       "of_grammatology"),
    ("russell",      "wrote",       "principia_mathematica"),
    ("beauvoir",     "wrote",       "the_second_sex"),
]