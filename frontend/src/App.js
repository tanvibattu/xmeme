import React, { Component, Fragment } from "react";
import Header from "./components/header";
import Home from "./components/home";
import './App.css';

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <Home />
      </Fragment>
    );
  }
}
export default App;



