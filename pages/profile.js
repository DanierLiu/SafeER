import Head from 'next/head';
import Layout from '../components/Layout';

export default function Profile() {
    return (
        <Layout>
            <Head>
                <title>Profile - SafeOR</title>
            </Head>
            <div>
                <h1>Profile</h1>
                {/* Add profile content here */}
            </div>
        </Layout>
    );
}
