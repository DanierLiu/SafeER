import Head from 'next/head';
import styles from '../styles/Home.module.css';
import Link from 'next/link';
import { useState } from "react";
import Layout from '../components/Layout';

export default function Home() {
  const [showPopup, setShowPopup] = useState(false);

  async function handleClick() {
    setShowPopup(true);

    // Start the vision.py script
    const response = await fetch('/api/start_vision_script', {
      method: 'POST'
    });

    // Open the procedure page in a new tab
    window.open('/procedure', '_blank');
  }

  return (
    <Layout home>
      <div className={styles.container} id="main_content">
        <Head>
          <title>SafeOR</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>

        <div className="text-left">
          <p className="text-lblue text-6xl mt-10 mb-5 font-semibold">Welcome to SafeER</p>
          <p className="text-blue text-6xl mt-10 mb-5 font-semibold">Shaping technology to save lives.</p>

          <div style={{ display: 'flex' }} className="items-center">
            <button className="bg-blue text-white font-bold rounded-full m-5 hover:bg-blue-500 text-blue-700 hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded text-left"
              onClick={handleClick}>
              Start Procedure
            </button>

            <Link href="/about">
              <button className="text-lblue font-bold py-2 px-4 border-2 border-blue-500 rounded text-left ml-5">
                About
              </button>
            </Link>
          </div>
        </div>
      </div>
    </Layout>
  );
}
