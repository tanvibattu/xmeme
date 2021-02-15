import React from "react";
import { Button, FormGroup, Input, Label} from "reactstrap";
import axios from "axios";
import Form from 'react-bootstrap/Form'
import { API_URL } from "../constants";

class MemeForm extends React.Component {
  
  state = {
    id: 0,
    name: "",
    caption: "",
    url: "",
  };
  
 
  componentDidMount() {
    if (this.props.memes) {
      const { id, name, caption, url } = this.props.memes;
      this.setState({ id, name, caption, url });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };
//  call create meme on submitting of form
  createMeme = e => {
    e.preventDefault();
      axios.post(API_URL, this.state).then(() => {
        this.props.resetState();
        this.setState({
          name:"",
          caption:"",
          url:'',
  
        });
      });
      
   
  };

  // set default value
  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <>
      <h2 style={{ color: "grey" }}>Post a meme</h2>

      {/* form for submiting meme with validation */}
      <Form onSubmit={this.createMeme} style={{color:"white"}} >
        <FormGroup>
          <Label for="name">Meme Owner:</Label>
          <Input
            type="text"
            name="name"
            onChange={this.onChange}
            placeholder="Enter your full name"
            value={this.defaultIfEmpty(this.state.name)}
            required  minLength={3}
          />
         
        </FormGroup>
        <FormGroup>
          <Label for="caption">Meme Caption:</Label>
          <Input
            type="caption"
            name="caption"
            onChange={this.onChange}
            placeholder="Enter a creative caption"
            value={this.defaultIfEmpty(this.state.caption)}
            required  minLength={5}
          />
        </FormGroup>
        <FormGroup>
          <Label for="url">Meme URL:</Label>
          <Input
            type="text"
            name="url"
            placeholder="Enter URL of your meme"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.url)}
            required pattern="https?://.+" 
          />
        </FormGroup>
       
        <Button type="submit">Send</Button>
      </Form>
      </>
    );
  }
}

export default MemeForm;

