import React from 'react';
import ListEvents from '../../components/ListEvents';

import upsellingIcon from '../../assets/icons/upselling-icon.png';

import './index.css';

function Upselling() {
  return (
    <ListEvents title="Upselling" typeIcon={upsellingIcon}/>
  );
}

export default Upselling;
