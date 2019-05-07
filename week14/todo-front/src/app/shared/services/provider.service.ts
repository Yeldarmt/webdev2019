import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {MainService} from './main.service';
import {IAuthResponse, ITask, ITaskList} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }
  getTaskLists(): Promise<ITaskList[]> {
    return this.get('http://localhost:8000/api/task_lists/', {});
  }
  getTasks(taskList: ITaskList): Promise<ITask[]> {
    return this.get(`http://localhost:8000/api/task_lists/${taskList.id}/tasks/`, {});
  }
  removeTaskList(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/task_lists/${id}/`, {});
  }
  createTaskList(namee: string): Promise<any> {
    return this.post('http://localhost:8000/api/task_lists/', {
      name: namee,
      tasks: []
    });
  }
  updateTaskList(taskList: ITaskList): Promise<any> {
    return this.put(`http://localhost:8000/api/task_lists/${taskList.id}/`, {
      name: taskList.name,
      tasks: taskList.tasks
    });
  }
  addTask(taskList: ITaskList, tn: string, tca: string, tdo: string, ts: string): Promise<ITask> {
    return this.post(`http://localhost:8000/api/task_lists/${taskList.id}/tasks/`, {
      name: tn,
      created_at: tca,
      due_on: tdo,
      status: ts,
      task_list_id: taskList.id
    });
  }
  search(taskList: ITaskList, searchName: string): Promise<ITask[]> {
    return this.get(`http://localhost:8000/api/task_lists/${taskList.id}/tasks/?search=${searchName}`, {});
  }
  auth(uname: string, pword: string): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: uname,
      password: pword
    });
  }
  logout(): Promise<any> {
    return this.post(`http://localhost:8000/api/logout/`, {});
  }
}
