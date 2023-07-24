import Link from 'next/link';
import Head from 'next/head';
import Script from 'next/script';
import Layout from '../components/Layout';
import { Bar, Line, Scatter, Bubble, Doughnut } from "react-chartjs-2"
import Chart from 'chart.js/auto';
import styles from '../styles/Home.module.css';

const doughData = {
  backgroundColor: [
    "rgb(2,88,255)",
    "rgb(249,151,0)",
    "rgb(255,199,0)",
    "rgb(32,214,152)",
  ],
  labels: ["Medial Error", "Incompetence", "Fatigue", "Medicial Error"],
  datasets: [
    {

      data: [3, 7, 2, 4],
      backgroundColor: [
        "rgb(2,88,255)",
        "rgb(249,151,0)",
        "rgb(255,199,0)",
        "rgb(32,214,152)",
      ],
      hoverOffset: 1,
    },
  ],
};

const doughOptions = {
  elements: {
    arc: {
      weight: 0.05,
      borderWidth: 1,
    },
  },
  cutout: 100,
};
const data = {
  labels: ["5 mins", "10 mins", "20 mins", "25 mins"],
  datasets: [
    {
      data: [3, 5, 6, 12],
    },
  ],
};


const options = {
  plugins: {
    legend: {
      display: false,
    },
  },
  elements: {
    line: {
      tension: 0,
      borderWidth: 2,
      pby: 50,
      borderColor: "rgba(47,97,68,1)",
      fill: "start",
      backgroundColor: "rgba(47,97,68,0.3)",
    },
    point: {
      radius: 0,
      hitRadius: 0,
    },
  },

  scales: {
    xAxis: {
      display: false,

    },
    yAxis: {
      display: false,
    },
    y: {
      suggestedMin: 1,
      suggestedMax: 10,
    },
  },
}

export default function Report() {
  return (
    <Layout>


      <Head>
        <title>Report</title>
      </Head>
      <div align="center">
        <img src="images/smalll.jpg" />

        <p class="text-[#008CA4] text-4xl text-center mt-10">Analytics</p>
      </div>
      <div class=" grid w-xl  grid-cols-3 gap-2 mt-4">
        <div class=" max-w-sm rounded overflow-hidden shadow-md mb-10">
          <div class="m-1">
            <div class="font-bold text-xl m-2 ">Total time spent on last operation</div>
            <p class="text-gray-700 text-base m-2"> 43 minutes </p>
          </div>


        </div>
        <div class=" max-w-sm rounded overflow-hidden shadow-md mb-10">
          <div class="font-bold text-xl m-2">Possible fatigue errors</div>
          <p class="text-gray-700 text-base m-2"> 5 </p>
        </div>
        <div class=" max-w-sm rounded overflow-hidden shadow-md mb-10">
          <div class="font-bold text-xl m-2">Possible equipment/human error</div>
          <p class="text-gray-700 text-base m-2"> 5 </p>
        </div>
      </div>
      <div class=" flex-box m-10  rows-2 text-base grid w-full max-w-screen-xl d grid-cols-2 gap-5 px-2 md:grid-cols-2 xl:px-3 ">
        <h3 class=" text-xl m-2 py-10"> Time into the procedure vs Fatigue Levels</h3>
        <div className='item'> <Line data={data} width={100} height={40} options={options} />
        </div>
        <h3 class=" text-xl m-20 py-10" > Comparision of faults</h3>
        <div className='item'> <Doughnut data={doughData} width={10} height={10} options={doughOptions} /></div>


      </div>

    </Layout>
  );
}
