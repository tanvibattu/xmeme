import React, { Component } from "react";
import Navbar from 'react-bootstrap/Navbar';
import '../App.css';

// sticky navbar with titke and logo on top of website
class Header extends Component {
  
  render() {
    return (      
      <> 
        <Navbar  sticky="top"className="top-navbar">
          <Navbar.Brand href="#home" className="navbar-brand">
            <img
              alt=""
              src="https://www.pinclipart.com/picdir/middle/73-733173_own-creation-funny-face-logo-meme-mania-clipart.png"
              width="50"
              height="50"
              className="d-inline-block align-top"
            />
            <span class="navbar-name"style={{padding:"30px"}} >XMeme</span>
          </Navbar.Brand>
        </Navbar>
      </>
    );
  }
}
export default Header;

