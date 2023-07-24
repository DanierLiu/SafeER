import styles from '../styles/Home.module.css';
import Head from 'next/head';


export default function Procedure({ }) {
  return (

    <div className={styles.container}>
      <Head>
        <title>SafeOR</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <h3 class="align-center font-bold text-3xl m-20 py-10">Starting Procedure...</h3>
    </div>
  )
}
