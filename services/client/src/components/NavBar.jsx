import React from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

import "./NavBar.css";

const titleStyle = {
  fontWeight: "bold"
};

const NavBar = props => {
  let menu = (
    <div className="navbar-menu">
      <div className="navbar-start">
        <Link to="/users" className="navbar-item" data-testid="nav-about">
          Users
        </Link>
        <Link to="/about" className="navbar-item" data-testid="nav-about">
          About
        </Link>
      </div>
    </div>
  );

  return (
    <nav
      className="navbar is-dark"
      role="navigation"
      aria-label="main navigation"
    >
      <section className="container">
        <div className="navbar-brand">
          <Link to="/" className="navbar-item nav-title" style={titleStyle}>
            {props.title}
          </Link>
          <span
            className="nav-toggle navbar-burger"
            onClick={() => {
              let toggle = document.querySelector(".nav-toggle");
              let menu = document.querySelector(".navbar-menu");
              toggle.classList.toggle("is-active");
              menu.classList.toggle("is-active");
            }}
          >
            <span />
            <span />
            <span />
          </span>
        </div>
        {menu}
      </section>
    </nav>
  );
};

NavBar.propTypes = {
  title: PropTypes.string.isRequired,
};

export default NavBar;
