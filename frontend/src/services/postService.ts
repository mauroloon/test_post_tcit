// services/posts.ts
interface Post {
  id: number;
  name: string;
  description: string;
}

export const getPosts = async (): Promise<Post[]> => {
  const response = await fetch('http://127.0.0.1:8000/api/posts');
  return response.json();
};

export const createPost = async (name: string, description: string): Promise<Post> => {
  const response = await fetch('http://127.0.0.1:8000/api/posts/create', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name, description })
  });
  return response.json();
};

export const deletePost = async (id: number): Promise<void> => {
  const response = await fetch(`http://127.0.0.1:8000/api/posts/${id}`, {
    method: 'DELETE',
  });
  if (!response.ok) {
    throw new Error('Error deleting post');
  }
};
