import { Injectable } from '@nestjs/common';

export interface UserProfile {
  id: number;
  fullName: string;
  phone: string;
  email: string;
  address: string;
}

const ALLOWED_FIELDS: Array<keyof UserProfile> = [
  'fullName',
  'phone',
  'email',
  'address',
];

@Injectable()
export class UserService {
  private currentUser: UserProfile = {
    id: 1,
    fullName: 'Nhân',
    phone: '0900000000',
    email: 'demo@example.com',
    address: 'Hà Nội',
  };

  getProfile(): UserProfile {
    return { ...this.currentUser };
  }

  updateField(field: string, value: string): UserProfile {
    if (!ALLOWED_FIELDS.includes(field as keyof UserProfile)) {
      throw new Error(
        `Field "${field}" không hợp lệ. Chỉ chấp nhận: ${ALLOWED_FIELDS.join(', ')}`,
      );
    }
    (this.currentUser as any)[field] = value;
    return this.getProfile();
  }
}
