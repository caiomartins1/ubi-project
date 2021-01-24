// TODO: Language dropdown

import React from 'react';
import { Link } from 'react-router-dom';

import exploreIcon from '../../assets/icons/explore-icon.png';
import upsellingIcon from '../../assets/icons/upselling-icon.png';
import highlightedIcon from '../../assets/icons/highlighted-icon.png';
import routesIcon from '../../assets/icons/routes-icon.png';
import ukFlagIcon from '../../assets/icons/uk-flag-icon.png';

import './index.css';

function Home() {
  return (
    <div className="home-page">
      <h1 className="home-title">Maldives Resort</h1>

      <div className="home-subheading-container">
        <h1 className="home-subheading1">Visit us,</h1>

        <p className="home-subheading2">have the holidays of <br/>your dreams here.</p>
      </div>

      <div className="home-main-buttons-container">
        <div className="home-horizontal-buttons-container">
          <Link to="/explore" className="home-buttom-link home-action-buttom">
            <img src={exploreIcon} alt="Explore" className="home-action-buttom-icon"/>

            <p className="home-action-buttom-title">Explore</p>
          </Link>

          <Link to="/explore" className="home-buttom-link home-action-buttom">
            <img src={upsellingIcon} alt="Upselling" className="home-action-buttom-icon"/>

            <p className="home-action-buttom-title">Upselling</p>
          </Link>
        </div>

        <div className="home-horizontal-buttons-container">
          <Link to="/explore" className="home-buttom-link home-action-buttom">
            <img src={highlightedIcon} alt="Highlighted" className="home-action-buttom-icon"/>

            <p className="home-action-buttom-title">Highlighted</p>
          </Link>

          <Link to="/explore" className="home-buttom-link home-action-buttom">
            <img src={routesIcon} alt="Routes" className="home-action-buttom-icon"/>

            <p className="home-action-buttom-title">Routes</p>
          </Link>
        </div>
      </div>

      <div className="home-language-buttom-container">
        <div className="home-language-buttom">
          <img src={ukFlagIcon} alt="UK" className="home-language-buttom-icon"/>

          <p className="home-language-buttom-text">English (UK)</p>
        </div>
      </div>
    </div>
  );
}

export default Home;
