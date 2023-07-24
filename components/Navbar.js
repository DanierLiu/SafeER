import Link from 'next/link';

const Navbar = () => {
    return (
        <nav className="bg-white fixed w-full z-20 top-0 left-0 border-b-4 border-blue">
            <div className="max-w-screen-xl flex justify-between items-center mx-auto p-4">
                <Link className="text-[#196279] text-lg font-semibold no-underline" href="/report">
                    View Report
                </Link>


                <div className="flex items-center space-x-4">
                    <Link className="text-[#196279] text-lg font-semibold text-decoration-line: none;" href="/">
                        SafeER
                    </Link>
                </div>

                <Link className="text-[#196279] text-lg font-semibold text-decoration-line: none;" href="/profile">
                    Profile
                </Link>

            </div>
        </nav>
    );
};

export default Navbar;
