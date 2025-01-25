import styles from './Table.module.css';

interface TableItem {
  id: number;
  name: string;
  description: string;
}

interface TableProps {
  data: TableItem[];
  onDelete: (id: number) => void;
}

export function Table({ data, onDelete }: TableProps) {
  return (
    <table className={styles.table}>
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Descripción</th>
          <th>Acción</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item) => (
          <tr key={item.id}>
            <td>{item.name}</td>
            <td>{item.description}</td>
            <td>
              <button 
                className={styles.deleteButton}
                onClick={() => onDelete(item.id)}
              >
                Eliminar
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}