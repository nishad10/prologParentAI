/*
	This is the things to ask related to each action category.
*/

play([playground,seasaw,toys,alphabet,hideandseek,sandbox,playmat,cars,trains,slides,build]).
eat([cake, toffee, candy, sandwich, pizza, cheerios, veggies, fries, noodles, meat]).
do([build, read, draw, dance,hideandseek,alphabet]).
see([river, well, farm, city,draw]).
argue([argue_with_friends,argue_with_teachers]).


/* 
	The followup questions for each category to be asked.
*/
pFollow(find_it_fun).
eFollow(eat_it_all).
dFollow(find_it_helpful).
sFollow(find_it_beautiful).
aFollow(get_punishment).

/* 
	Initialize all for multiple runs
*/
like(nothing).
dislike(nothing)..
history(nothing).


/*
	Ask something to start off the system as everything is initialized at the start.
*/

ask(playground, 0).

/* 
	As we already asked a random item we now ask a related item.
*/

ask(X,Y):-like(Y), related(X,Y), \+ history(X).

/* 
	Also keep track that we don't repeat them.
*/

ask(X,Y):- random(X), \+ related(X,Y), \+ history(X).

/* 
	Now we ask a random one after the followup to start again
*/

ask(X,Y):- random(X), \+ history(X).





/*
	Rule to append lists and add to it
*/
append([X | Y], Z, [X | W]) :- append(Y, Z, W).
append([], X, X).

/*
	See the relationship in between the two X and Y
*/

related(X,Y) :-
	play(L), member(X, L), member(Y, L);
	eat(L), member(X, L), member(Y, L);
	do(L), member(X, L), member(Y, L);
	see(L), member(X, L), member(Y, L);
	argue(L), member(X, L), member(Y, L).

/*
	X and Y relationship in between member and the followup category we declared earlier for each action
*/
followup(X, Y) :-
	play(L), member(X, L), pFollow(Y);
	eat(L), member(X, L), eFollow(Y);
	do(L), member(X, L), dFollow(Y);
	see(L), member(X, L),sFollow(Y);
	argue(L), member(X, L), aFollow(Y).

/* 
	Random 
*/

random(X) :-
	play(L), member(X, L);
	eat(L), member(X, L);
	do(L), member(X, L);
	see(L), member(X, L);
	argue(L), member(X, L).
