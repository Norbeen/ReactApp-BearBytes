import * as React from 'react';

export function Review(user, body, date, rating, foodId, image) {
	this.user = user;
	this.body = body;
	this.date = date;
	this.likes = 0;
	this.dislikes = 0;
	this.rating = rating;
	this.foodId = foodId;
	this.image = image;
}
