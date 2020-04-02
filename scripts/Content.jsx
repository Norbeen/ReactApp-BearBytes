import * as React from 'react';

export class Content extends React.Component {
    render() {
        return (<div>

    // !PAGE CONTENT! -->
    <div className="w3-main w3-content w3-padding" style={{maxWidth:'1200px;margin-top:100px'}}>
    
      // First Photo Grid-->
      <div className="w3-row-padding w3-padding-16 w3-center" id="food">
        <div className="w3-quarter">
          <img src="/w3images/sandwich.jpg" alt="Sandwich" style={{width:"100%"}}/>
          <h3>The Perfect Sandwich, A Real NYC classNameic</h3>
          <p>Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum.</p>
        </div>
        <div className="w3-quarter">
          <img src="/w3images/steak.jpg" alt="Steak" style={{width:"100%"}}/>
          <h3>Let Me Tell You About This Steak</h3>
          <p>Once again, some random text to lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum.</p>
        </div>
        <div className="w3-quarter">
          <img src="/w3images/cherries.jpg" alt="Cherries" style={{width:"100%"}}/>
          <h3>Cherries, interrupted</h3>
          <p>Lorem ipsum text praesent tincidunt ipsum lipsum.</p>
          <p>What else?</p>
        </div>
        <div className="w3-quarter">
          <img src="/w3images/wine.jpg" alt="Pasta and Wine" style={{width:"100%"}}/>
          <h3>Once Again, Robust Wine and Vegetable Pasta</h3>
          <p>Lorem ipsum text praesent tincidunt ipsum lipsum.</p>
        </div>
      </div>
      
      // Second Photo Grid-->
      <div className="w3-row-padding w3-padding-16 w3-center">
        <div className="w3-quarter">
          <img src="/w3images/popsicle.jpg" alt="Popsicle" style={{width:"100%"}}/>
          <h3>All I Need Is a Popsicle</h3>
          <p>Lorem ipsum text praesent tincidunt ipsum lipsum.</p>
        </div>
        <div className="w3-quarter">
          <img src="/w3images/salmon.jpg" alt="Salmon" style={{width:"100%"}}/>
          <h3>Salmon For Your Skin</h3>
          <p>Once again, some random text to lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum.</p>
        </div>
        <div className="w3-quarter">
          <img src="/w3images/sandwich.jpg" alt="Sandwich" style={{width:"100%"}}/>
          <h3>The Perfect Sandwich, A Real classNameic</h3>
          <p>Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum.</p>
        </div>
        <div className="w3-quarter">
          <img src="/w3images/croissant.jpg" alt="Croissant" style={{width:"100%"}}/>
          <h3>Le French</h3>
          <p>Lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum.</p>
        </div>
      </div>
    
      // Pagination -->
      <div className="w3-center w3-padding-32">
        <div className="w3-bar">
          <a href="#" className="w3-bar-item w3-button w3-hover-black">«</a>
          <a href="#" className="w3-bar-item w3-black w3-button">1</a>
          <a href="#" className="w3-bar-item w3-button w3-hover-black">2</a>
          <a href="#" className="w3-bar-item w3-button w3-hover-black">3</a>
          <a href="#" className="w3-bar-item w3-button w3-hover-black">4</a>
          <a href="#" className="w3-bar-item w3-button w3-hover-black">»</a>
        </div>
      </div>
      
    
	    
		    // preloader section -->
		<section className="preloader">
			<div className="sk-spinner sk-spinner-pulse"></div>
		</section>
		
		// navigation section -->
		<section className="navbar navbar-default navbar-fixed-top" role="navigation">
			<div className="container">
				<div className="navbar-header">
					<button className="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
						<span className="icon icon-bar"></span>
						<span className="icon icon-bar"></span>
						<span className="icon icon-bar"></span>
					</button>
					<a href="#" className="navbar-brand">ZENTRO</a>
				</div>
				<div className="collapse navbar-collapse">
					<ul className="nav navbar-nav navbar-right">
						<li><a href="#home" className="smoothScroll">HOME</a></li>
						<li><a href="#gallery" className="smoothScroll">FOOD GALLERY</a></li>
						<li><a href="#menu" className="smoothScroll">SPECIAL MENU</a></li>
						<li><a href="#team" className="smoothScroll">CHEFS</a></li>
						<li><a href="#contact" className="smoothScroll">CONTACT</a></li>
					</ul>
				</div>
			</div>
		</section>
		</div>
    </div>)
    }
}