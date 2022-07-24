import React from 'react';
import './Graph.css';

export default class Graph extends React.Component {
  render() {
    return (
        <div>
            <p>Scatter graph for now</p>
            <svg className="axis" height={500} width={500}>
                {this.props.points.map((point) => <circle cx={point.x} cy={500-point.y} r={3}/>)}
            </svg>
        </div>
    );
  }
}
