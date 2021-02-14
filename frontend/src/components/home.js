import React, { Component } from "react";
import MemeList from "./memeList";
import axios from "axios";
import { API_URL } from "../constants";
import MemeForm from "./form";

class Home extends Component {
  state = {
    memes: []
  };

  componentDidMount() {
    this.resetState();
  }

  // method to get all memes to show on screen
  getMemes = () => {
    axios.get(API_URL).then(res => this.setState({ memes: res.data }));
  };

  resetState = () => {
    this.getMemes();
  };

  // show screen in 2 parts one:post meme, second: show meme
  render() {    
    return (
      <>
        <div class="split left">
          < div class="centered">
              <MemeForm create={true} resetState={this.resetState}  />
            </div>
        </div>
        
        <div class="split right">
          <div class="centered">
            <MemeList
              memes={this.state.memes}
              resetState={this.resetState}
            />
          </div>
        </div> 
      </>  
    );
  }
}

export default Home;