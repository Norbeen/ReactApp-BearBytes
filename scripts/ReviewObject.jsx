import * as React from 'react';

export function Review(user, body, date, rating, foodTitle, image) {
	this.user = user;
	this.body = body;
	this.date = date;
	this.likes = 0;
	this.dislikes = 0;
	this.rating = rating;
	this.foodTitle = foodTitle;
	this.image = image;
}
