 has_fur(tiger).
has_feathers(bird).
can_fly(bird).
lays_eggs(bird).
has_scales(fish).
swims(fish).

% Define rules for inferring new information.
mammal(X) :- has_fur(X).
mammal(X) :- gives_milk(X).
bird(X) :- has_feathers(X), lays_eggs(X), can_fly(X).
reptile(X) :- has_scales(X), lays_eggs(X), not(mammal(X)).
fish(X) :- has_scales(X), lays_eggs(X), not(mammal(X)), not(bird(X)).

% Query to perform forward chaining and infer new information.
inferred_mammal(X) :- mammal(X).
inferred_bird(X) :- bird(X).
inferred_reptile(X) :- reptile(X).
inferred_fish(X) :- fish(X).
