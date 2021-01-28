import React from 'react';

import offlineImg from '../../assets/offline-img.svg';

import './index.css';

function Off({ msg }) {

  return (
    <div className="offline-message-container">
      <img src={offlineImg} alt="" className="offline-message-image"/>
      <h1 className="offline-message">{msg}</h1>
    </div>

  );
}

export default Off;
