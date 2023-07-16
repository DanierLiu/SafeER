import styles from '../styles/Home.module.css';
import Head from 'next/head';

export default function about() {
  return (
    <div className={styles.container}>
      <Head>
        <title>SafeOR</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <h3 className="text-center font-bold text-3xl m-20 py-10">Why SafeOR?</h3>
      <h4>SafeOR uses modern technologies such as computer vision, NLP, and machine learning.</h4>
    </div>
  );
}
