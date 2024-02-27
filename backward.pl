has_feathers(bird).
can_fly(bird).
lays_eggs(bird).
has_scales(fish).
swims(fish).

% Define rules for inferring new information.
bird(X) :- has_feathers(X), lays_eggs(X), can_fly(X).
fish(X) :- has_scales(X), swims(X).

% Define a goal for backward chaining.
is_bird(X) :- bird(X).
is_fish(X) :- fish(X).
