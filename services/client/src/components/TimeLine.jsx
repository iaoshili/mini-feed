import React from "react";
import PropTypes from "prop-types";

const TimeLines = props => {
  return (
    <div>
      <table className="table is-hoverable is-fullwidth">
        <thead>
          <tr>
            <th>ID</th>
            <th>content</th>
          </tr>
        </thead>
        <tbody>
          {props.tweets.map(tweet => {
            return (
              <tr key={tweet.id}>
                <td>{tweet.id}</td>
                <td>{tweet.content}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

TimeLines.propTypes = {
  tweets: PropTypes.array.isRequired,
};

export default TimeLines;
