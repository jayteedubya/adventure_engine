The map file is a single line blob in a text file. it is filled with the ascii characters
that are used to represent different entities. Spaces will be used as passable areas. It
will all be render with ncurses. Additionally, we need a style sheet of some kind for configurability.
Something that can map basic entity types to characters and set colors. Perhaps the answer
is to have entity classes that carry the color and character for the entity. Non-entities
will have to be handled somehow. Two handling paths is worrysome. A better abstraction will
need to be figured. On the one hand, populating all locations as an entity would give a 
universal path so that all things can be interactive. On the other hand, maybe we can split 
entities out and have event triggers instead to handle entities interacting with boundaries.