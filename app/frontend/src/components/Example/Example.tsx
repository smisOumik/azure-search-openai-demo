import React from 'react';
import ReactDOM from 'react-dom';
import styles from './Example.module.css';

interface Props {
  text: string | JSX.Element;
  onClick?: () => void;
}

const Example: React.FC<Props> = ({ text, onClick }) => {
  const copyToClipboard = () => {
    let textToCopy: string;
    if (typeof text === 'string') {
      textToCopy = text;
    } else {
      // If text is a JSX.Element, convert it to a string
      const tempDiv = document.createElement ('div');
      ReactDOM.render (<>{text}</>, tempDiv);
      textToCopy = tempDiv.innerText;
    }
    
    navigator.clipboard.writeText(textToCopy).then(() => {
      console.log('Text copied to clipboard');
    });
    onClick && onClick ();
  };

  return (
    <div className={styles.example} onClick={copyToClipboard}>
      <p className={styles.exampleText}>
        {typeof text === 'string' ? text : text}
      </p>
    </div>
  );
};

export default Example;