import styles from '../styles/Home.module.css';
import Head from 'next/head';
import Layout from '../components/Layout';

export default function About() {
  return (
    <Layout>
      <div className={`${styles.container} mx-auto my-0 px-4 sm:px-6 py-10`}>
        <Head>
          <title>SafeOR - About</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>

        <h3 className="font-bold text-3xl mt-20 py-10">What is SafeER?</h3>

        <h4 className="text-m">SafeOR uses modern technologies such as computer vision, NLP, and machine learning to bring visibility to patient safety and the need for tech-enabled solutions to reduce medical errors.
          When we look at the number of deaths caused by medical errors, it's alarmingly high and doesn't seem to be decreasing. <b>How do we do it?</b> We train the computer to <b>recognize patterns of fatigue and incompetence caused by external factors.</b> The computer, combined with a high-definition lens fitted in the operating room, is able to track those patterns and tackle some of those challenges in real-time with feedback, as well as generate a report at the end of every procedure.</h4>

        <div className='footer'>Developed by Danielx2, Kelly, and Abhitej.</div>
      </div>
    </Layout>
  );
}

