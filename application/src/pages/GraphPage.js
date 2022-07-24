import React from 'react';
import Graph from '../components/Graph';
import './GraphPage.css';


export default class GraphPage extends React.Component {
  constructor(props){
    super(props);
    // the default points should be empty
    this.state = {
      points: [{x: 10, y: 10},{x: 50, y: 100},{x: 200, y: 50}, {x: 300, y: 200}, {x: 350, y: 200}, {x: 480, y: 250}],
      file: "",
    }
  }

  handleOnChange = (e) => {
    this.setState({ file: e.target.files[0]})
  }

  handleOnSubmit = (e) => {
    e.preventDefault();
    if (this.state.file) {
        const fileReader = new FileReader()
        fileReader.onload = function (event) {
            const csvOutput = event.target.result
            // TODO some treatment of the actual input to send to backend
            console.log(csvOutput)
        };

        fileReader.readAsText(this.state.file)
        // TODO await for backend response and pass it to points
    }
  }

  render() {
    return (
      <div>        
        <form onSubmit={this.handleSubmit}>
          <input type={"file"} accept={".csv"} onChange={this.handleOnChange}/>
          <button onClick={this.handleOnSubmit}> IMPORT CSV</button>
        </form>
        <div className='basePage'>
          <Graph points={this.state.points} />
        </div>
      </div>
    );
  }
}
