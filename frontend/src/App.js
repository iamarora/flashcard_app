import React, { Component } from "react";
import axios from "axios";

import {
  Button,
} from "reactstrap";

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      form: {"id":"", "word":"", "definition": ""},
      error: "",
      show_definition: false,
    };
  }

  componentDidMount() {
    this.fetchWordData();
  }

  fetchWordData = () => {
    let THIS = this;
    THIS.setState({ show_definition: false })
    axios
      .get("http://localhost:8000/fetch_word/")
      .then( function (res) {
        let data = res.data;
        console.log(data)
        if ("error" in data) {
          THIS.setState({ error: data.error })
        } else {
          THIS.setState({ form: data })
        }
      })
      .catch((err) => console.log(err));
  };

  showDefinition = () => {
    this.setState({show_definition: true})
  }

  updateWordStatus = (status) => {
    let THIS = this;
    axios.put('http://localhost:8000/update_word/', {"id": this.state.form.id, "status": status})
    .then(function (response) {
      THIS.fetchWordData()
    })
    .catch(function (error) {
      console.log(JSON.stringify(error))
      console.log(error.message)
      alert(error);
    });
  }

  correctDefinition = () => {
    this.updateWordStatus(true)
  }

  wrongDefinition = () => {
    this.updateWordStatus(false)
  }

  render() {
    return (
      <main className="container">
        <h1 className="text-center my-4">Flashcard app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-6">
              <div className="card-body">
                <h5 className="card-title">{this.state.form.word}</h5>
                {this.state.error ? null : <Button type="button" onClick={this.showDefinition} color="info">Show definition</Button>}
                { this.state.show_definition ? (<div>
                  <p className="card-text">{this.state.form.definition}</p>
                  <Button className="float-left" type="button" onClick={this.correctDefinition} color="success">I got it</Button>
                  <Button className="float-right" type="button" onClick={this.wrongDefinition} color="danger">I did not get it</Button>
                </div>) : null }
              </div>
            </div>
            <span>{this.state.error ? this.state.error: null}</span>
          </div>
        </div>
      </main>
    );
  }
}

export default App;