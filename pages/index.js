import Head from 'next/head';
import styles from '../styles/Home.module.css';
import Link from 'next/link';
import { getSortedPostsData } from '../lib/posts';
import Layout from '../components/layout';
import { useState } from "react";

export async function getStaticProps() {
  const allPostsData = getSortedPostsData();
  return {
    props: {
      allPostsData,
    },
  };
}

export default function Home({ allPostsData }) {
  const [showPopup, setShowPopup] = useState(false);

  async function handleClick() {
    setShowPopup(true);

    const data = await fetch('url')
  }

  return (

    <div className={styles.container} id="main_content">

      <Head>
        <title>SafeOR</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      {/* <img class="mt-10" src="images/logo.jpg" /> */}
      <div className="text-left">
        <p className="text-[#5CC3C6] text-6xl mt-10 mb-5 font-semibold">Welcome to SafeER</p>
        <p className="text-[#0191A8] text-6xl mt-10 mb-5 font-semibold">Shaping technology to save lives.</p>

        <div style={{ display: 'flex' }} className="items-center">
          <Link href="/procedure">
            <button className="bg-[#0194AE] text-white font-bold rounded-full m-5 hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded text-left">
              Start Procedure
            </button>
          </Link>

          <Link href="/about">
            <button className="text-[#4AB8B9] font-bold py-2 px-4 border border-blue-500 rounded text-left ml-5">
              About
            </button>
          </Link>
        </div>
      </div>

      {/* <h3 class="align-center font-bold text-3xl mt-20">What is SafeOR? </h3>
      <h4 class="text-m mr-10 ml-10 mt-10">SafeOR uses modern technologies such as computer vision, NLP, and machine learning to bring visibility to the patient safety and need for tech enabled solutions to reduce medical error.
        When we look the numbers of deaths that are caused due to medical error, they are at an insane amount and do not seem to be decreasing. <b> How we do it? </b> We worked the computer to <b>recognize patterns of fatigue, and incompetence
          if any caused by external factors. </b>The computer, combined with a high definition lens fitted in the operating room is able to track those patterns and tackle some of those challenges real-time with feedback and some through
        a report generate at the end of every procedure.  </h4>
      <Link href="/faq">
        <button class="bg-[#5CC3C6] text-white font-bold  rounded-full m-5">
          FAQ
        </button>
      </Link>
      <div class='footer'>Developed by Danielx2, Kelly and Abhitej.</div>
  */}
    </div>

  )
}
