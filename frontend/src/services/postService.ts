// services/posts.ts
interface Post {
  id: number;
  name: string;
  description: string;
}

/**
 * Retorna todos los posts
 */
export const getPosts = async (): Promise<Post[]> => {
  const response = await fetch('http://127.0.0.1:8000/api/posts');
  return response.json();
};

/**
 * Crea un post
 * @param name 
 * @param description 
 */
export async function createPost(name: string, description: string): Promise<Post> {
  const response = await fetch('http://127.0.0.1:8000/api/posts/create', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name, description }),
  });
  const data = await response.json();
  return data;
}

/**
 * Elimina un post
 * @param id 
 */
export const deletePost = async (id: number): Promise<void> => {
  const response = await fetch(`http://127.0.0.1:8000/api/posts/${id}`, {
    method: 'DELETE',
  });
  if (!response.ok) {
    throw new Error('Error deleting post');
  }
};
