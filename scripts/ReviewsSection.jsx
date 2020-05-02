import * as React from 'react';
import { Socket } from './Socket';
import { useState } from 'react';
import { Review } from './ReviewObject';

function Rating(props){
  if(props.rating == 0){
    return(
      <img src="https://i.ibb.co/89PP1RD/0Rating.png" alt="Rating" style={{width:"50%"}}/>
      )
  } 
  
  if(props.rating == 1){
    return(
    <img src="https://i.ibb.co/9hPds0L/2Rating.png" alt="Rating" style={{width:"50%"}}/>
    )
  } 
  
  if(props.rating == 2){
    return(
    <img src="https://i.ibb.co/9hPds0L/2Rating.png" alt="Rating" style={{width:"50%"}}/>
    )
  } 
  
  if(props.rating == 3){
    return(
    <img src="https://i.ibb.co/1Rq3tcb/3Rating.png" alt="Rating" style={{width:"50%"}}/>
    )
  } 
  
  if(props.rating == 4){
    return(
    <img src="https://i.ibb.co/qr7QcSn/4Rating.png" alt="Rating" style={{width:"50%"}}/>
    )
  } 
  
  if(props.rating == 5){
    return(
    <img src="https://i.ibb.co/K97vCGR/5Rating.png" alt="Rating" style={{width:"50%"}}/>
    )
  }
  return(<p style={{color: "#0B76F4", width: "80%", marginLeft:"auto", marginRight: "auto"}}>(Rating unavailable)</p>)
}

function Image(props){
  if(!props.image){
    return(
      <div />
      )
  }
  return(
    <img src={props.image} alt="Food Item" style={{width:"200px",height:"200px", paddingBottom: "5%", objectFit: "cover"}}/>
    )
}

function ReviewCard(props){
  const [likesCount, setLikesCount] = useState(props.likesCount)
  const [dislikesCount, setDislikesCount] = useState(props.dislikesCount)
  const [previousLike, setPreviousLike] = useState(false)
  const [previousDislike, setPreviousDislike] = useState(false)
  
  const updateLikes = () =>{
    if(previousLike){
      console.log('previous likes updated')
      setLikesCount(likesCount - 1)
      setPreviousLike(false)
      
      Socket.emit('new like/disike', {
      "likes": likesCount-1,
      "dislikes": dislikesCount,
      "review_id": props.id
    })
    }
    
    else if(previousDislike){
      setLikesCount(likesCount + 1)
      setPreviousLike(true)
      setDislikesCount(dislikesCount -1)
      setPreviousDislike(false)
      console.log('dislike deducted')
      
      Socket.emit('new like/disike', {
      "likes": likesCount+1,
      "dislikes": dislikesCount-1,
      "review_id": props.id
    })
    }
    
    else if(!previousLike){
      console.log('non previous like updated')
      setLikesCount(likesCount + 1)
      setPreviousLike(true)
      
      Socket.emit('new like/disike', {
      "likes": likesCount+1,
      "dislikes": dislikesCount,
      "review_id": props.id
    })
    }
  }
  
  const updateDislikes = () =>{
    if(previousDislike){
      console.log('previous likes updated')
      setDislikesCount(dislikesCount - 1)
      setPreviousDislike(false)
      Socket.emit('new like/disike', {
      "likes": likesCount,
      "dislikes": dislikesCount-1,
      "foodId": props.foodId
    })
    }
    
    else if(previousLike){
      setDislikesCount(dislikesCount + 1)
      setPreviousDislike(true)
      setLikesCount(likesCount -1)
      setPreviousLike(false)
      console.log('like deducted')
      
      Socket.emit('new like/disike', {
      "likes": likesCount-1,
      "dislikes": dislikesCount+1,
      "foodId": props.foodId
    })
    }
    
    else if(!previousDislike){
      console.log('non previous dislike updated')
      setDislikesCount(dislikesCount + 1)
      setPreviousLike(true)
      
      Socket.emit('new like/disike', {
      "likes": likesCount,
      "dislikes": dislikesCount+1,
      "foodId": props.foodId
    })
    }
  }
  
  
  return( 
  <div className="w3-third" style={{paddingTop:"2%"}}>
    <div className="food-card">
      <div className="w3-row" >
        <div className="w3-col" style={{width:"40%"}} >
          <img src={props.pp} alt="profile picture" style={{height: "80px", width:"80px", borderRadius: "50%", paddingTop: "5%", paddingBottom: "5%", objectFit: "cover", float:"right"}}/>
        </div>
        <div className="w3-col" style={{width:"60%"}}>
          <div className="w3-row" >
            <h5 style={{color: "#F46311"}}>{props.name}</h5>
          </div>
          <div className="w3-row">
            <h6 style={{color: "#F46311"}}>{props.reviewDate}</h6>
            <input type="image" src="https://i.ibb.co/88Bp8w2/thumb-up-24px-1.png" 
            alt="Rating" style={{width:"10%", paddingRight:"4px"}}
            onClick={() => updateLikes()}
            />
            <h7 style={{color: "#F46311", paddingRight:"10px"}}>{likesCount}</h7>
            <input type="image" src="https://i.ibb.co/p4yrh6Z/thumb-down-24px-1.png" 
            alt="Rating" style={{width:"10%", paddingRight:"4px"}}
            onClick={() => updateDislikes()}
            />
            <h7 style={{color: "#F46311"}}>{dislikesCount}</h7>
          </div>
        </div>
      </div>
      <div className="review-divider"/>
        <div className="w3-row" >
            <Rating rating={props.rating} />
        </div>
        <p style={{color: "#F46311", width: "80%", marginLeft:"auto", marginRight: "auto", paddingTop: "2%", fontWeight: "bold", fontSize:"16px", paddingBottom:"10px"}}>{props.reviewText}</p>
        <Image image={props.image} />
    </div>
  </div>
  )
}

export class ReviewsSection extends React.Component { 
    constructor(props) {
    super(props);
    this.state = {
      current_food_id: "",
      newest_reviews_list: [],
      popular_reviews_list: [],
      positive_reviews_list: [],
      negative_reviews_list: [],
      current_order: [],
      order_track:'new'
    };
    
    this.componentDidMount = this.componentDidMount.bind(this)
    this.handleReviewOrder = this.handleReviewOrder.bind(this)
  }
  componentDidMount() {
      Socket.on('send review list',(data) => {
      console.log('review received')
      this.setState({
        newest_reviews_list: data['newest_reviews'],
        popular_reviews_list: data['popular_reviews'],
        positive_reviews_list: data['positive_reviews'],
        negative_reviews_list: data['negative_reviews']
      })
      console.log('review received', this.state.newest_reviews_list)
      
      if (this.handleReviewOrder(this.state.order_track) == 'new'){
        this.setState({
          current_order: this.state.newest_reviews_list
        })
      }
      
      else if (this.handleReviewOrder(this.state.order_track) == 'popular'){
        this.setState({
          current_order: this.state.newest_reviews_list
        })
      }
      
      else if (this.handleReviewOrder(this.state.order_track) == 'positive'){
        this.setState({
          current_order: this.state.newest_reviews_list
        })
      }
      
      else if (this.handleReviewOrder(this.state.order_track) == 'negative'){
        this.setState({
          current_order: this.state.newest_reviews_list
        })
      }
    })
    this.setState({
      current_order: this.state.newest_reviews_list
    })
    Socket.on('menu item',(data) => {
        console.log('received menu data in reviews', data["menu_item"])
        this.setState({
          current_food_id: data['menu_item']["id"]
        });
      })
    Socket.on('send review',(data) => {
      console.log('review received')
      this.state.newest_reviews_list.unshift(data['review'])
      this.state.popular_reviews_list.push(data['review'])
      this.state.positive_reviews_list.push(data['review'])
      this.state.negative_reviews_list.push(data['review'])
        this.setState({
        newest_reviews_list: this.state.newest_reviews_list,
        popular_reviews_list: this.state.popular_reviews_list,
        positive_reviews_list:  this.state.positive_reviews_list,
        negative_reviews_list: this.state.negative_reviews_list
      })
      console.log('review received', this.state.newest_reviews_list)
    })
  }
  
  handleReviewOrder(order){
    console.log("order value:", order)
    if (order == 'new'){
      console.log('sort by new')
        this.setState({
          current_order: this.state.newest_reviews_list,
          order_track: 'new'
        })
        return 'new'
      }
      
      else if (order == 'popular'){
        console.log('sort by poppin')
        this.setState({
          current_order: this.state.popular_reviews_list,
          order_track: 'popular'
        })
        return 'popular'
      }
      
      else if (order == 'positive'){
        console.log('sort by positive')
        this.setState({
          current_order: this.state.positive_reviews_list,
          order_track: 'positive'
        })
        return 'positive'
      }
      
      else if (order == 'negative'){
        console.log('sort by negative')
        this.setState({
          current_order: this.state.negative_reviews_list,
          order_track: 'negative'
        })
        return 'negative'
      }
    }
  
    render() {
      console.log("current order", this.state.current_order)
        return (
    <div>
        <div className="btn-group btn-group-toggle" data-toggle="buttons" style={{backgroundColor:"#F46311", width:"100%"}}>
            <label className="btn btn-secondary active segmented-control" onClick={ () => this.handleReviewOrder('new')}>
              <input type="radio" value="new" id="1" autoComplete="off" defaultChecked
               checked={this.props.checked == "new"}
              /> Newest
            </label>
            <label className="btn btn-secondary segmented-control" onClick={ () => this.handleReviewOrder('popular')}>
              <input type="radio" value="popular" id="2" autoComplete="off"
               checked={this.props.checked == "popular"}
              /> Most Popular
            </label>
            <label className="btn btn-secondary segmented-control" onClick={ () => this.handleReviewOrder('positive')}>
              <input type="radio" value="positive" id="3" autoComplete="off"
               checked={this.props.checked == "positive"}
              /> Most Positive
            </label>
            <label className="btn btn-secondary segmented-control" onClick={ () => this.handleReviewOrder('negative')}>
              <input type="radio" value="critical" id="4" autoComplete="off"
               checked={this.props.checked == "critical"}
              /> Most Critical
            </label>
        </div>
        <div className="w3-row-padding w3-center">
          { this.state.current_order.map ( review =>
                  <ReviewCard key={review.id} name={review.username} pp={review.profilePic}
                  likesCount={review.likes} dislikesCount={review.dislikes} reviewDate={review.date} reviewText={review.body}
                  image={review.image} rating={review.rating} id={review.id} />
            )}
        </div>
    </div>)
  }
}