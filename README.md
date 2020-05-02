# Bear Bites

## Collaborators
* George Martin
* Nabin Baral
* Kayla thompson
* Kedar Timalsena

## Deliverables
Our mission for this project is to promote the university cafeteria and dining, so we want students to have access to information on what is being served and be able to rate accordingly. Whilst  it is based on student’s reviews, we are simultaneously suggesting the university dine and cafeteria on the kinds of food students would like the university to have. It will let students and guests try out the most voted food while keeping the promise of the university to serve better food.

## Motivation
Too many times students have said “aww man I wish I went to the canteen” or “I wasted my time going to the refac, I didn’t like what they were serving.” This app will help students make a better decision when selecting what dining hall to go to. 

## Approach
We are going to  build a food ratings app using Flask in the backend and React/JS in the frontend, alongside Socket.io for duplex communication between client and server. We will also be incorporating several API like Twilio. The app will feature a social login via Google, and will be deployed on Heroku. 

## Dependencies and risks
This app will depend on the menu of Morgan State University’s cafeteria as it will show the meal available in the cafeteria on that particular day. We want to keep these reviews as authentic as possible as it could put some  popular and commonly served meals at risk. We are using React as a novice, so the implementation can be a little tough. We are also using technologies like Twilio, learnt during the coursework and being new to many technologies, it is always a challenge for beginners like us. Alongside, deploying via Heroku could be a little tricky, which we can expect to have on this project as well,  but we are hoping to give 100% to make this project a success. 

## User Stories
The following **required** user stories are complete:
- [x] As a user, I should be able to login with google, so that my credentials allow me to interact with the application.
- [x] As a user, I should be able to see the menu for the day, so I can make an informed decision on where I should eat 
- [x] As a user, I should be able to see ratings for menu items, so I can make an so I can rank what options I'd like to eat in case one food item is out
- [x] As a user, I should be able to see comments for menu items, so I can make an informed decision on what I should eat 
- [x] As a user,  I should be able to post comments and ratings for menu items, so I can help other users make an informed decision on what they should eat  
- [x] As a user, I should be able to like/dislike comments for menu items, so I can cosign on previous comments and don’t have to write my own 
- [ ] As a user, I should be able to see the top rated foods for the day, so I can quickly see the best options 
- [x] As a user I can filter comments by likes, dislikes, or time posted so I can see a variety of comments.

## Checkpoint 1
### The checkpoint 1 will constituent following implementations:
* Get the website layout up and running using react(front end) and flask(backend)
* Implement styling to beautify the website for better end user experience
* Implementation of socket.io to talk between serverside and client side.
* Database implementation
* Create json for menu items





