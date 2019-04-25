# General Assembly WDI Project 4: A Flack + React App

[Portfolio Link](http://wdi-tag.herokuapp.com/)

Work in progress...

Tag was my final project of the Web Development Immersive course at General Assembly. It was my first project to feature Python and Flask for the backend, and SQL for my API database. I worked solo to make sure I had a firm grasp on everything the app incorporated.

---

## Brief

In 8 days I had to:

* **Build a full-stack application** by making your own backend and your own front-end
* **Use a Python Flask API** to serve your data from a Postgres database
* **Consume your API with a separate front-end** built with React
* **Be a complete product** which most likely means multiple relationships and CRUD functionality for at least a couple of models
* **Implement thoughtful user stories/wireframes** that are significant enough to help you know which features are core MVP and which you can cut
* **Have a visually impressive design** to kick your portfolio up a notch and have something to wow future clients & employers. **ALLOW** time for this.
* **Be deployed online** so it's publicly accessible.

## Technologies Used:

* JavaScript
* React
* HTML
* CSS
* Sass
* Python
* Flask
* SQL
* Materialize
* Mapbox
* OpenCage Geocoder
* Axios
* Filestack

## Approach Taken

Inspired by the amazing street art that features on walls around the Shoreditch area, for my final solo project I wanted to create an app that would allow people to find and appreciate street art easier. Using Python/Flask for the back end and JavaScript/React for the front end, I built Tag, a web app which allows users to find street art in their local area and elsewhere, plus also share their own spots.

<!-- As a user you can search all areas of central London for spots, browse the spots in more detail, browse the artist and see their other work, search spots, upload additional images to existing spots, and add your own spots. Other technologies used included SQL, Sass, Mapbox, OpenCage Geocoder, Materialize & Axios.

I hadn’t worked with maps before, which proved quite challenging but very rewarding as I love the idea of building apps that interact with the real world in some way. I’m really pleased with how it turned out, especially its responsiveness on mobile, which was a key design factor. Going forward with the project, I definitely want to add recommended walking routes for certain areas and also the ability to add authenticated artists. -->


---

## Screenshot Walk-through

### Landing page for logged-out users prompting register/login.

![landing page](screenshots/landing-page.png)

### Register page that allows user to register their details.

![register](screenshots/register.png)

### Login page allows user to login.

![login](screenshots/login.png)

### The user's homescreen is a centered map on the user's location, displaying all the nearby graffiti spots. The user also is given the option to search or create a new spot.

![newsfeed](screenshots/homescreen.png)

### The show spot page displays all the relevant information for that spot, including images, location, artists, categories. The page also allows the user to like the spot, add additional images to the spot and leave a comment. If the user is the creator of the spot or images they have the option to edit or delete the spot.

![recipe page](screenshots/show-spot.png)

### The show artist modal, which activates once the artist is clicked, allows the user to read a short bio on the artist and also browse his other work.

![review page](screenshots/show-artist.png)

### The search page defaults to all results and allows the user to browse freely and narrow down results by spot name, artist or categories.

![profile page](screenshots/search.png)

### The New Spot Form allows you to add new spots.

![search](screenshots/new-spot.png)

___

### Functionality

The functionality works seamlessly with the real world to allow the user to:

* Register & login
* Search all areas of central London for spots
* Browse the spots in more detail
* Browse the artist and see their other work
* Search spots based on spot name, artist or category
* Upload additional images to existing spots
* Add your own spots

### Process
When we realised there were very few apps that incorporated both restaurant reviews and recipes (apps tend to lean to one or the other), we realised we had our USP. Once we had settled on our concept, we got to work on the project.
1.  To work efficiently and effectively as a team, we used Trello to assign the various tasks amongst us. This was particularly useful when we were working remotely.
![trello](screenshots/trello.png)
2.  In order to understand how our app would work at a fundamental level we needed to draft out models and routes in a visual manner.
![backend wireframe](screenshots/backend-wireframe.jpeg)
3.  We then created wireframes for the front end to visualise how our backend would interact with it.
4.  By day 2 we were happy with our respective wireframes, we began work on our backend: creating the models, controllers, and then routes, all in Node.js.
5.  By the end of day 4 we had tested the backend using Insomnia and we were happy with the functionality. We then started work on the frontend: creating the app.js file, then creating the various components that would make up the app, all in React.
6.  After day 6 we had reached an MVP level of completion, we began styling the app using the Bulma framework.

#### Featured piece of code 1

The User Schema was by far our most complicated model, as it had to contain the majority of datasets. It contained referenced models, as well as virtuals (for reviews and recipes) and a friends plugin. The friends plugin took quite a while to implement as the documentation wasn't as clear as I would have hoped. This was also my first experience with virtuals, which was quite challenging to understand at first.

``` JavaScript

const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true, trim: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  name: { type: String, required: true },
  categories: [ {
    type: mongoose.Schema.ObjectId,
    ref: 'Category',
    required: true
  } ],
  image: { type: String },
  location: { type: String },
  bio: { type: String },
  pinnedRecipes: [ {
    type: mongoose.Schema.ObjectId,
    ref: 'Recipe'
  } ],
  pinnedReviews: [ {
    type: mongoose.Schema.ObjectId,
    ref: 'Review',
    required: true
  } ]
})

userSchema.plugin(friendsPlugin({ pathName: 'friends' }))

userSchema.virtual('reviews', {
  ref: 'Review',
  localField: '_id',
  foreignField: 'user'
})

```

### Styling

We used the CSS framework Bulma to style our app. This would take some of the heavy lifting out of creating things like navbars etc., so we could focus more on the functionality of the site. We customised the default Bulma settings as much as we could to differentiate itself from other Bulma products - which generally look quite similar. This involved customising the buttons to feature icons, changing the curvature of the cards, and some of the navbar configuration.

In future I would avoid using Bulma as we found it quite difficult to customise once we had applied its classes, and ended up being quite a time drain. In my next project I will try and use a different CSS framework like Materialise.

#### Featured piece of code 2

This is how we got our curated Newsfeed to work. It pulls in all the data from our API for recipes, reviews and user using an ```axios.all``` request. It then checks if the user is friends with the user who wrote the recipe/review - if yes, then then item will show. If not, it will check if the review shares any of the same categories as the user's preferences. It will finally check if the user is the author, and disregard the item if it's true.

``` JavaScript

componentDidMount() {
  axios.all([
    axios.get(`/api/user/${Auth.getPayload().sub}`),
    axios.get('/api/recipes'),
    axios.get('/api/reviews')
  ])
    .then(res => {
      const [ user, recipes, reviews ] = res
      const recipeFeed = recipes.data.filter(recipe => {
        return ((user.data.friends.some(friend => {
          return (recipe.user.id.includes(friend._id) && friend.status !== 'pending')
        })) || user.data.user.categories.some(category => {
          return recipe.categories.some(categoryObject => {
            return Object.values(categoryObject).includes(category._id)
          })
        }) && recipe.user.id !== Auth.getPayload().sub)
      })
      const reviewFeed = reviews.data.filter(review => {
        return ((user.data.friends.some(friend => {
          return (review.user.id.includes(friend._id) && friend.status !== 'pending')
        })) || user.data.user.categories.some(category => {
          return review.categories.some(categoryObject => {
            return Object.values(categoryObject).includes(category._id)
          })
        }) && review.user.id !== Auth.getPayload().sub)
      })
      this.setState({ recipeFeed, reviewFeed, user })
    })
}

```
___

### Wins and Blockers

One of the biggest blockers for this project was creating a substantial seeds file that incorporated promised. As some models relied on other models in order to be created, we had to establish multiple promises in the seeds file in order for the database to accept certain models. For instance, in order for a review to exist, it must first have a user and categories in order to create the review - so we would create the user and categories first and then promise them to the review seed.

``` JavaScript
     return Promise.all([
        Review.create([
          {
            'restaurantName': 'Noble Rot',
            'reviewHeadline': 'So good!',
            'reviewText': 'The very best restaurants are like your oldest friend.',
            'rating': 5,
            'image': 'https://infatuation.imgix.net/media/images/reviews/noble-rot-wine-bar/banners/1492493931.11.jpg?auto=format&h=840&w=1336',
            'user': users[getRandom(4)]._id,
            'categories': [categories[5]._id,categories[3]._id,categories[63]._id,categories[89]._id
          }
        )]
      )]
```

As for wins, I'm really pleased with how the backend works and allows the user to do everything a normal social media platform would. The friends request system and the pinned items are particularly slick, allowing users to customise their experience of the site easily and efficiently. The newsfeed also works really nicely, making it feel like a real service.
___

## Future Features

If we had more time essential future features we would like to add include:

* Adding an external API, such as Zomato, to display locations of restaurants.
* Ability to un-pin items and un-like reviews/recipes.
* A shopping list functionality so you could keep all the ingredients you needed for your next shop on your app.
* A simple cooking timer on the recipe pages to assist with timekeeping.
