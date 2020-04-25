import * as React from 'react';
import { Socket } from './Socket';
import { useState } from 'react';

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
    }else if(previousDislike){
      setLikesCount(likesCount + 1)
      setPreviousLike(true)
      setDislikesCount(dislikesCount -1)
      setPreviousDislike(false)
      console.log('dislike deducted')
    }else if(!previousLike){
      console.log('non previous like updated')
      setLikesCount(likesCount + 1)
      setPreviousLike(true)
    }
  }
  
  const updateDislikes = () =>{
    if(previousDislike){
      console.log('previous likes updated')
      setDislikesCount(dislikesCount - 1)
      setPreviousDislike(false)
    }else if(previousLike){
      setDislikesCount(dislikesCount + 1)
      setPreviousDislike(true)
      setLikesCount(likesCount -1)
      setPreviousLike(false)
      console.log('like deducted')
    }else if(!previousDislike){
      console.log('non previous dislike updated')
      setDislikesCount(dislikesCount + 1)
      setPreviousLike(true)
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
          <h5 style={{color: "#F46311"}}>{props.name}</h5>
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
      menu_data: [],
      reviews_list: []
    };
    
    this.componentDidMount = this.componentDidMount.bind(this)
  }
  componentDidMount() {
      Socket.on('send review',(data) => {
      console.log('review received')
      this.setState({
        reviews_list: data['review']
      })
    })
  }
  
    render() {
        return (
    <div>
        <div className="btn-group btn-group-toggle" data-toggle="buttons" style={{backgroundColor:"#F46311", width:"100%"}}>
            <label className="btn btn-secondary active segmented-control">
              <input type="radio" name="newest" id="1" autoComplete="off" defaultChecked/> Newest
            </label>
            <label className="btn btn-secondary segmented-control">
              <input type="radio" name="popular" id="2" autoComplete="off"/> Most Popular
            </label>
            <label className="btn btn-secondary segmented-control">
              <input type="radio" name="positive" id="3" autoComplete="off"/> Most Positive
            </label>
            <label className="btn btn-secondary segmented-control">
              <input type="radio" name="critical" id="4" autoComplete="off"/> Most Critical
            </label>
        </div>
        { this.state.reviews_list.map ( review =>
            <div className="w3-row-padding w3-center">
                <ReviewCard name={review.user.name} pp={review.user.profilePic}
                likesCount={review.likes} dislikesCount={review.dislikes} reviewDate={review.date} reviewText={review.body}
                image={review.image} rating={review.rating} />
            </div>
          )}
    </div>)
    }
}