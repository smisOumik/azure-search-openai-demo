import React from 'react';
import styles from './Example.module.css';

interface Props {
  text: string;
}

const Example: React.FC<Props> = ({ text }) => {
  const copyToClipboard = () => {
    navigator.clipboard.writeText(text).then(() => {
      // Optionally, you can add some visual feedback here
      console.log('Text copied to clipboard');
    });
  };

  return (
    <div className={styles.example} onClick={copyToClipboard}>
      <p className={styles.exampleText}>{text}</p>
    </div>
  );
};

export default Example;