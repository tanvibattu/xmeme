import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";
import axios from "axios";
import { API_URL } from "../constants";

class EditForm extends React.Component {
  state = {
    id: 0,
    caption: "",
    url: "",
  };

  componentDidMount() {
    if (this.props.memes) {
      const { id, caption, url } = this.props.memes;
      this.setState({ id,  caption, url });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };


  editMeme = e => {
    e.preventDefault();
    axios.patch(API_URL + this.state.id, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.editMeme} style={{color:"black"}}>
        
        <h3>{this.state.name}</h3>

        <FormGroup>
          <Label for="caption">Caption:</Label>
          <Input
            type="caption"
            name="caption"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.caption)}
            required  minLength={4}
          />
        </FormGroup>
        <FormGroup>
          <Label for="url">Url:</Label>
          <Input
            type="text"
            name="url"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.url)}
            required pattern="https?://.+" 

          />
        </FormGroup>
       
        <Button type="submit">Send</Button>
      </Form>
    );
  }
}

export default EditForm;

