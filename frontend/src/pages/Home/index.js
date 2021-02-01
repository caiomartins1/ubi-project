import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import langs from '../../lang/lang';

import exploreIcon from '../../assets/icons/explore-icon.png';
import upsellingIcon from '../../assets/icons/upselling-icon.png';
import highlightedIcon from '../../assets/icons/highlighted-icon.png';
import routesIcon from '../../assets/icons/routes-icon.png';
import ukFlagIcon from '../../assets/icons/uk-flag-icon.png';
import ptFlagIcon from '../../assets/icons/pt-flag-icon.png';
import frFlagIcon from '../../assets/icons/france-flag-icon.png';
import deFlagIcon from '../../assets/icons/germany-flag-icon.png';

import './index.css';


function Home() {

  const langOptions = {
    'en': {
      'icon': ukFlagIcon,
      'title': 'English (UK)'
    },
    'pt': {
      'icon': ptFlagIcon,
      'title': 'Portuguese (PT)'
    },
    'de': {
      'icon': deFlagIcon,
      'title': 'German'
    },
    'fr': {
      'icon': frFlagIcon,
      'title': 'French'
    },
  };

  const [lang, setLang] = React.useState(
    localStorage.getItem('lang') || 'en'
  );
 
  const [translatedText, setTranslatedText] = useState({});

  useEffect(() => {
    localStorage.setItem('lang', lang);
    getTranslatedText(lang);
  }, [lang]);

  function getTranslatedText(lang) {
    setTranslatedText(langs['home'][lang]);
  }

  function handleLanguageChange(event) {
    setLang(event.target.value);
  }

  return (
    <div className="home-page">
      <h1 className="home-title">Maldives Resort</h1>

      <div className="home-subheading-container">
        <h1 className="home-subheading1">{translatedText['subheading-1']},</h1>

        <p className="home-subheading2">{translatedText['subheading-2']}</p>
      </div>

      <div className="home-main-buttons-container">
        <div className="home-horizontal-buttons-container">
          <Link to="explore" className="home-buttom-link home-action-buttom home-action-buttom-left">
            <img src={exploreIcon} alt="Explore" className="home-action-buttom-icon"/>

            <p className="home-action-buttom-title">{translatedText['explore']}</p>
          </Link>

          <Link to="/upselling" className="home-buttom-link home-action-buttom home-action-buttom-right">
            <img src={upsellingIcon} alt="Upselling" className="home-action-buttom-icon"/>

            <p className="home-action-buttom-title">{translatedText['upselling']}</p>
          </Link>
        </div>

        <div className="home-horizontal-buttons-container">
          <Link to="/highlighted" className="home-buttom-link home-action-buttom home-action-buttom-left">
            <img src={highlightedIcon} alt="Highlighted" className="home-action-buttom-icon"/>

            <p className="home-action-buttom-title">{translatedText['highlighted']}</p>
          </Link>

          <Link to="/routes" className="home-buttom-link home-action-buttom home-action-buttom-right">
            <img src={routesIcon} alt="Routes" className="home-action-buttom-icon"/>

            <p className="home-action-buttom-title">{translatedText['routes']}</p>
          </Link>
        </div>
      </div>

      <div className="home-languague-buttom">
        <img src={langOptions[lang].icon} alt={langOptions[lang].title} className="home-language-buttom-icon"/>

        <select className="home-language-buttom-input" value={lang} onChange={handleLanguageChange}>
          <option value="en">{langOptions['en'].title}</option>
          <option value="pt">{langOptions['pt'].title}</option>
          <option value="de">{langOptions['de'].title}</option>
          <option value="fr">{langOptions['fr'].title}</option>
        </select>
      </div>
    </div>
  );
}

export default Home;
