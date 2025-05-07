import { useEffect, useState } from "react";

export default function AdminDashboard() {
  const [dataAbsensi, setDataAbsensi] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/absensi/hari-ini")
      .then((res) => res.json())
      .then((data) => setDataAbsensi(data))
      .catch((err) => console.error("Gagal fetch data:", err));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Data Absensi Hari Ini</h1>
      <div className="overflow-x-auto">
        <table className="min-w-full bg-white border border-gray-300 rounded-lg">
          <thead className="bg-gray-100 text-gray-700 text-left">
            <tr>
              <th className="px-4 py-2">Nama</th>
              <th className="px-4 py-2">Waktu Masuk</th>
              <th className="px-4 py-2">Status</th>
            </tr>
          </thead>
          <tbody>
            {dataAbsensi.map((siswa, index) => (
              <tr key={index} className="border-t hover:bg-gray-50">
                <td className="px-4 py-2">{siswa.nama}</td>
                <td className="px-4 py-2">{siswa.waktu_masuk}</td>
                <td className={`px-4 py-2 font-semibold ${
                  siswa.status === "Tepat Waktu" ? "text-green-600" : "text-red-600"
                }`}>
                  {siswa.status}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
