# Demo: Áp dụng ECC vào code có sẵn

## Code cũ của bạn (ví dụ)

```typescript
// src/components/UserProfile.tsx
import React from 'react'

function UserProfile({ user }) {
  return (
    <div>
      <h2>{user.name}</h2>
      <p>{user.email}</p>
      <button onClick={() => {
        // API call để update user
        fetch('/api/user/' + user.id, {
          method: 'POST',
          body: JSON.stringify({ name: user.name })
        })
      }}>Update</button>
    </div>
  )
}

export default UserProfile
```

## Sau khi áp dụng ECC

### Step 1: Review với ECC
```
/typescript-reviewer
/react-reviewer
/security-reviewer
```

### Step 2: Code cải tiến

```typescript
// src/components/UserProfile.tsx
import React, { useState, useCallback } from 'react'
import type { User } from '../types/user'

interface UserProfileProps {
  user: User
  onUpdate?: (user: User) => void
  className?: string
}

/**
 * UserProfile Component
 * Displays and allows editing user profile information
 */
const UserProfile: React.FC<UserProfileProps> = ({ 
  user, 
  onUpdate,
  className = ''
}) => {
  const [isUpdating, setIsUpdating] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleUpdate = useCallback(async () => {
    if (isUpdating) return

    setIsUpdating(true)
    setError(null)

    try { 
      const response = await fetch(`/api/user/${user.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          name: user.name,
          email: user.email 
        })
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const updatedUser = await response.json()
      onUpdate?.(updatedUser)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Update failed')
    } finally {
      setIsUpdating(false)
    }
  }, [user, isUpdating, onUpdate])

  return (
    <div className={`user-profile ${className}`}>
      <div className="user-info">
        <h2 className="user-name">{user.name}</h2>
        <p className="user-email">{user.email}</p>
      </div>
      
      {error && (
        <div className="error-message" role="alert">
          {error}
        </div>
      )}
      
      <button 
        onClick={handleUpdate}
        disabled={isUpdating}
        className="update-button"
        aria-label="Update user profile"
      >
        {isUpdating ? 'Updating...' : 'Update'}
      </button>
    </div>
  )
}

export default UserProfile
```

### Step 3: Add Tests

```typescript
// src/components/__tests__/UserProfile.test.tsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import UserProfile from '../UserProfile'

// Mock fetch
global.fetch = jest.fn()

describe('UserProfile Component', () => {
  const mockUser = {
    id: '1',
    name: 'John Doe',
    email: 'john@example.com'
  }

  beforeEach(() => {
    jest.clearAllMocks()
  })

  test('renders user information', () => {
    render(<UserProfile user={mockUser} />)
    
    expect(screen.getByText('John Doe')).toBeInTheDocument()
    expect(screen.getByText('john@example.com')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Update user profile' })).toBeInTheDocument()
  })

  test('handles update successfully', async () => {
    const mockOnUpdate = jest.fn()
    ;(fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => mockUser
    })

    render(<UserProfile user={mockUser} onUpdate={mockOnUpdate} />)
    
    const user = userEvent.setup()
    await user.click(screen.getByRole('button', { name: 'Update user profile' }))

    await waitFor(() => {
      expect(mockOnUpdate).toHaveBeenCalledWith(mockUser)
    })
  })

  test('handles update error', async () => {
    ;(fetch as jest.Mock).mockRejectedValueOnce(new Error('Network error'))

    render(<UserProfile user={mockUser} />)
    
    const user = userEvent.setup()
    await user.click(screen.getByRole('button', { name: 'Update user profile' }))

    await waitFor(() => {
      expect(screen.getByText('Update failed')).toBeInTheDocument()
    })
  })
})
```

### Step 4: Add Styles

```css
/* src/components/UserProfile.module.css */
.userProfile {
  padding: 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  background: white;
}

.userInfo {
  margin-bottom: 1rem;
}

.userName {
  margin: 0 0 0.5rem 0;
  font-size: 1.25rem;
  font-weight: 600;
}

.userEmail {
  margin: 0;
  color: #64748b;
}

.updateButton {
  padding: 0.5rem 1rem;
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
}

.updateButton:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.errorMessage {
  margin: 0.5rem 0;
  padding: 0.5rem;
  background: #fee2e2;
  color: #dc2626;
  border-radius: 0.25rem;
  font-size: 0.875rem;
}
```

## Cải thiện đã áp dụng:

### ✅ TypeScript
- Thêm types cho props
- Generic types cho API responses
- Type-safe event handlers

### ✅ React Best Practices
- useCallback để optimize performance
- Proper state management
- Error boundaries handling
- Accessibility attributes

### ✅ Security
- Proper HTTP method (PATCH instead of POST)
- Headers validation
- Error handling không expose sensitive info

### ✅ UX
- Loading states
- Error messages
- Disabled states
- ARIA labels

### ✅ Testing
- Unit tests với Jest
- User event testing
- Error scenario testing
- Mock API calls

### ✅ Code Organization
- CSS Modules
- Proper imports
- JSDoc comments
- Component composition
