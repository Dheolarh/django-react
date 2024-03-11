import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

const novels = [
  {
  img: "https://th.bing.com/th/id/OIP.4CFAaeZ9n7GfbgchwaOungHaJ4?rs=1&pid=ImgDetMain",
  title: "Avatar",
  subtitle: "The Last Airbender",
  producer: "Nickelodeon Animation Studio",
  },

  {
  img: "https://th.bing.com/th?id=OIF.RRTTIOCBONGivf%2bQO%2bRRCg&rs=1&pid=ImgDetMain",
  title: "Shōgun",
  producer: "FX Networks",
  }
]
const Novel = function ({ img, title, subtitle, producer }) {
  return (
    <div className="novel">
      <img src={img} alt={title} />
      <h3>{title.toUpperCase()}</h3>
      <span className="sub">{subtitle}</span>
      <p>{producer}</p>
    </div>
  );
};

const Novels = function () {
  return (
    <div className="novelBlock">
        {novels.map((novels) => {
          return books
        })}
    </div>
  );
};

let Home = function () {
  return (
    <React.Fragment>
      <Novels />
    </React.Fragment>
  );
};

// Note that you can only return one tag, a React.Fragment tag can serve as the main tag to return if you
// don't want to use a div tag
// Instead of using class='' as attribute we use className=''

ReactDOM.render(<Home />, document.getElementById("root"));
