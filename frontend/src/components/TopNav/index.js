import React from 'react';
import { useHistory } from 'react-router-dom';


import leftArrowIcon from '../../assets/icons/left-arrow-icon.png';

import './index.css';

function TopNav({ title, typeIcon}) {

  const history = useHistory();
  return (
      <nav className="top-nav">
        <img src={leftArrowIcon} alt="" className="top-nav-back-icon" onClick={() => history.goBack()}/>

        <h1 className="top-nav-title">{title}</h1>

        <img src={typeIcon} alt="" className="top-nav-type-icon"/>
      </nav>

  );
}

export default TopNav;
